[CmdletBinding(PositionalBinding = $false)]
param(
    [Parameter(Position = 0)]
    [ValidateSet("todos")]
    [string] $Mode,

    [Parameter()]
    [string] $Root,

    [Parameter()]
    [string] $DocsRoot,

    [Parameter()]
    [int] $MinChars = 40
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding $false
$OutputEncoding = [Console]::OutputEncoding

$DefaultDocsDir = "docs"
$TodoPattern = [regex]::new("\b(?:TODO|TBD|FIXME)\b", [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)
$HeadingPattern = [regex]::new("^(?<indent> {0,3})(?<marker>#+)(?<rest>.*)$")
$FencePattern = [regex]::new('^\s*(```+|~~~+)')
$FileNamePattern = [regex]::new("^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
$UriSchemePattern = [regex]::new("^[a-z][a-z0-9+.-]*:", [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)

function New-ValidationError {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path,

        [Parameter(Mandatory = $true)]
        [string] $Message
    )

    [pscustomobject]@{
        Path = $Path
        Message = $Message
    }
}

function Get-RelativePosixPath {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileSystemInfo] $Path,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $RootDirectory
    )

    $rootPath = $RootDirectory.FullName.TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar)
    $fullPath = $Path.FullName

    if ($fullPath -eq $rootPath) {
        return "."
    }

    $prefix = $rootPath + [System.IO.Path]::DirectorySeparatorChar
    if (-not $fullPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Cesta neni pod korenem projektu: $fullPath"
    }

    return $fullPath.Substring($prefix.Length).Replace("\", "/")
}

function Get-OrdinalSortKey {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Value
    )

    $builder = [System.Text.StringBuilder]::new()
    foreach ($character in $Value.ToCharArray()) {
        [void] $builder.Append(([int][char] $character).ToString("x6"))
    }

    return $builder.ToString()
}

function Get-CodePointColumn {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Value,

        [Parameter(Mandatory = $true)]
        [int] $Index
    )

    $column = 1
    for ($cursor = 0; $cursor -lt $Index; $cursor++) {
        if (-not [char]::IsLowSurrogate($Value[$cursor])) {
            $column++
        }
    }

    return $column
}

function Test-CaseSensitiveLeafPath {
    param(
        [Parameter(Mandatory = $true)]
        [string] $Path
    )

    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $pathRoot = [System.IO.Path]::GetPathRoot($fullPath)
    if ([string]::IsNullOrWhiteSpace($pathRoot)) {
        return $false
    }

    $remainingPath = $fullPath.Substring($pathRoot.Length)
    $segments = @($remainingPath -split "[\\/]+" | Where-Object { $_ -ne "" })
    $currentPath = $pathRoot
    $currentItem = $null

    foreach ($segment in $segments) {
        $currentItem = Get-ChildItem -LiteralPath $currentPath -Force |
            Where-Object { $_.Name -ceq $segment } |
            Select-Object -First 1

        if ($null -eq $currentItem) {
            return $false
        }

        $currentPath = $currentItem.FullName
    }

    return $currentItem -is [System.IO.FileInfo]
}

function Get-MarkdownFiles {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory
    )

    if (-not $DocsDirectory.Exists) {
        throw "Adresar s dokumentaci neexistuje: $($DocsDirectory.FullName)"
    }

    return Get-ChildItem -LiteralPath $DocsDirectory.FullName -Recurse -File -Filter "*.md" |
        Sort-Object { $_.FullName.ToLowerInvariant() }
}

function Test-FenceLine {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Line
    )

    return $FencePattern.IsMatch($Line)
}

function Test-Escaped {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Value,

        [Parameter(Mandatory = $true)]
        [int] $Index
    )

    $backslashCount = 0
    $cursor = $Index - 1
    while ($cursor -ge 0 -and $Value[$cursor] -eq "\") {
        $backslashCount++
        $cursor--
    }

    return ($backslashCount % 2) -eq 1
}

function Find-ClosingParen {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Value,

        [Parameter(Mandatory = $true)]
        [int] $OpenParenIndex
    )

    $depth = 1
    $cursor = $OpenParenIndex + 1

    while ($cursor -lt $Value.Length) {
        $character = $Value[$cursor]
        if (($character -eq "(" -or $character -eq ")") -and (Test-Escaped -Value $Value -Index $cursor)) {
            $cursor++
            continue
        }

        if ($character -eq "(") {
            $depth++
        }
        elseif ($character -eq ")") {
            $depth--
            if ($depth -eq 0) {
                return $cursor
            }
        }

        $cursor++
    }

    return -1
}

function Get-MarkdownLinks {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Line
    )

    $links = New-Object System.Collections.Generic.List[object]
    $cursor = 0

    while ($cursor -lt $Line.Length) {
        $isImage = $Line[$cursor] -eq "!" -and $cursor + 1 -lt $Line.Length -and $Line[$cursor + 1] -eq "["
        $isLink = $Line[$cursor] -eq "["
        if (-not $isImage -and -not $isLink) {
            $cursor++
            continue
        }

        $start = $cursor
        $labelStart = if ($isImage) { $cursor + 1 } else { $cursor }
        $labelEnd = $Line.IndexOf("]", $labelStart + 1)
        if ($labelEnd -eq -1) {
            break
        }

        if ($labelEnd + 1 -ge $Line.Length -or $Line[$labelEnd + 1] -ne "(") {
            $cursor = $labelEnd + 1
            continue
        }

        $openParen = $labelEnd + 1
        $closeParen = Find-ClosingParen -Value $Line -OpenParenIndex $openParen
        if ($closeParen -eq -1) {
            break
        }

        $rawTarget = $Line.Substring($openParen + 1, $closeParen - $openParen - 1)
        $links.Add([pscustomobject]@{
                RawTarget = $rawTarget
                Column = Get-CodePointColumn -Value $Line -Index $start
            })
        $cursor = $closeParen + 1
    }

    return $links.ToArray()
}

function Get-LinkDestination {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $RawTarget
    )

    $strippedTarget = $RawTarget.Trim()
    if ($strippedTarget.Length -eq 0) {
        return ""
    }

    if ($strippedTarget.StartsWith("<", [System.StringComparison]::Ordinal)) {
        $endIndex = $strippedTarget.IndexOf(">")
        if ($endIndex -ne -1) {
            return $strippedTarget.Substring(1, $endIndex - 1).Trim()
        }
    }

    return ([regex]::Split($strippedTarget, "\s+", 2))[0]
}

function Test-ExternalOrAnchorLink {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Target
    )

    return $Target.StartsWith("#", [System.StringComparison]::Ordinal) `
        -or $Target.StartsWith("//", [System.StringComparison]::Ordinal) `
        -or $UriSchemePattern.IsMatch($Target)
}

function Get-LinkPathWithoutFragment {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Target
    )

    return (($Target -split "#", 2)[0] -split "\?", 2)[0]
}

function Test-LinkHasExtension {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $TargetPath
    )

    $normalizedTarget = $TargetPath.Replace("\", "/")
    $lastSegment = ($normalizedTarget -split "/")[-1]
    $extension = [System.IO.Path]::GetExtension($lastSegment)
    return $extension -ne "" -and $extension -ne "."
}

function Test-LinkHasMarkdownExtension {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $TargetPath
    )

    $normalizedTarget = $TargetPath.Replace("\", "/")
    $lastSegment = ($normalizedTarget -split "/")[-1]
    return [System.IO.Path]::GetExtension($lastSegment).ToLowerInvariant() -eq ".md"
}

function Test-LinkHasUnsupportedDotSegment {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $TargetPath
    )

    $normalizedTarget = $TargetPath.Replace("\", "/")
    foreach ($segment in ($normalizedTarget -split "/")) {
        if ($segment -match "^\.\.\.+$") {
            return $true
        }
    }

    return $false
}

function Get-LinkCandidatePaths {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $TargetPath
    )

    $normalizedTarget = $TargetPath.Replace("\", "/")
    $isAbsolute = $normalizedTarget.StartsWith("/", [System.StringComparison]::Ordinal)
    $relativeTarget = if ($isAbsolute) { $normalizedTarget.TrimStart("/") } else { $normalizedTarget }
    $basePath = if ($isAbsolute) { $DocsDirectory.FullName } else { $Path.DirectoryName }

    foreach ($part in ($relativeTarget -split "/" | Where-Object { $_ -ne "" })) {
        $basePath = Join-Path -Path $basePath -ChildPath $part
    }

    $candidates = New-Object System.Collections.Generic.List[string]
    $candidates.Add($basePath)
    if (-not (Test-LinkHasExtension -TargetPath $normalizedTarget)) {
        if (-not $normalizedTarget.EndsWith("/", [System.StringComparison]::Ordinal)) {
            $candidates.Add("$basePath.md")
        }
        $candidates.Add((Join-Path -Path $basePath -ChildPath "index.md"))
    }

    return $candidates.ToArray()
}

function Resolve-DocumentationLink {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory,

        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $TargetPath
    )

    if (Test-LinkHasUnsupportedDotSegment -TargetPath $TargetPath) {
        return $null
    }

    $resolvedDocsRoot = $DocsDirectory.FullName.TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar)
    foreach ($candidate in (Get-LinkCandidatePaths -Path $Path -DocsDirectory $DocsDirectory -TargetPath $TargetPath)) {
        if (-not (Test-CaseSensitiveLeafPath -Path $candidate)) {
            continue
        }

        $resolvedCandidate = [System.IO.Path]::GetFullPath($candidate)
        if (
            $resolvedCandidate -eq $resolvedDocsRoot `
                -or $resolvedCandidate.StartsWith($resolvedDocsRoot + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)
        ) {
            return $resolvedCandidate
        }
    }

    return $null
}

function Test-Links {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Line,

        [Parameter(Mandatory = $true)]
        [int] $LineNumber,

        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory
    )

    $errors = New-Object System.Collections.Generic.List[object]
    foreach ($link in (Get-MarkdownLinks -Line $Line)) {
        $target = Get-LinkDestination -RawTarget $link.RawTarget
        if ($target.Length -eq 0) {
            $errors.Add(
                (New-ValidationError `
                        -Path $Path `
                        -Message "Rozbity odkaz na radku $LineNumber, sloupec $($link.Column): prazdny cil")
            )
            continue
        }

        if (Test-ExternalOrAnchorLink -Target $target) {
            continue
        }

        $targetPath = Get-LinkPathWithoutFragment -Target $target
        if ($targetPath.Length -eq 0) {
            continue
        }

        if (Test-LinkHasMarkdownExtension -TargetPath $targetPath) {
            $errors.Add(
                (New-ValidationError `
                        -Path $Path `
                        -Message "Podezrely odkaz s priponou .md na radku $LineNumber, sloupec $($link.Column)")
            )
        }

        $resolvedTarget = Resolve-DocumentationLink -Path $Path -DocsDirectory $DocsDirectory -TargetPath $targetPath
        if ($null -eq $resolvedTarget) {
            $errors.Add(
                (New-ValidationError `
                        -Path $Path `
                        -Message "Rozbity odkaz na radku $LineNumber, sloupec $($link.Column)")
            )
        }
    }

    return $errors.ToArray()
}

function Test-FileName {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path
    )

    if ($FileNamePattern.IsMatch($Path.Name)) {
        return @()
    }

    return @(
        New-ValidationError `
            -Path $Path `
            -Message "Neplatne jmeno souboru: pouzij lowercase bez diakritiky a slova oddeluj pomlckou"
    )
}

function Test-Heading {
    param(
        [Parameter(Mandatory = $true)]
        [AllowEmptyString()]
        [string] $Line,

        [Parameter(Mandatory = $true)]
        [int] $LineNumber,

        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path
    )

    $match = $HeadingPattern.Match($Line.TrimEnd("`r", "`n"))
    if (-not $match.Success) {
        return @()
    }

    $marker = $match.Groups["marker"].Value
    $rest = $match.Groups["rest"].Value
    $errors = New-Object System.Collections.Generic.List[object]

    if ($marker.Length -gt 6) {
        $errors.Add((New-ValidationError -Path $Path -Message "Chyba v nadpisu na radku ${LineNumber}: nadpis muze mit nejvyse 6 znaku #"))
        return $errors.ToArray()
    }

    if ($rest.Length -gt 0 -and -not [char]::IsWhiteSpace($rest[0])) {
        $errors.Add((New-ValidationError -Path $Path -Message "Chyba v nadpisu na radku ${LineNumber}: chybi mezera za #"))
        return $errors.ToArray()
    }

    $headingText = $rest.Trim()
    if ($headingText.Length -eq 0) {
        $errors.Add((New-ValidationError -Path $Path -Message "Chyba v nadpisu na radku ${LineNumber}: chybi text nadpisu"))
        return $errors.ToArray()
    }

    if ($headingText.EndsWith("#", [System.StringComparison]::Ordinal)) {
        $strippedClosing = $headingText.TrimEnd("#").TrimEnd()
        if ($strippedClosing.Length -eq 0) {
            $errors.Add((New-ValidationError -Path $Path -Message "Chyba v nadpisu na radku ${LineNumber}: chybi text nadpisu"))
        }
        elseif (-not ([regex]::IsMatch($headingText, "\s#+$"))) {
            $errors.Add((New-ValidationError -Path $Path -Message "Chyba v nadpisu na radku ${LineNumber}: neplatne ukonceni nadpisu znakem #"))
        }
    }

    return $errors.ToArray()
}

function Test-MarkdownFile {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.FileInfo] $Path,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory,

        [Parameter(Mandatory = $true)]
        [bool] $IncludeTodos,

        [Parameter(Mandatory = $true)]
        [int] $MinChars
    )

    $text = Get-Content -LiteralPath $Path.FullName -Raw -Encoding utf8
    if ($null -eq $text) {
        $text = ""
    }

    $strippedText = $text.Trim()
    $errors = New-Object System.Collections.Generic.List[object]

    if ($strippedText.Length -eq 0) {
        $errors.Add((New-ValidationError -Path $Path -Message "Soubor je prazdny"))
        return $errors.ToArray()
    }

    if ($strippedText.Length -lt $MinChars) {
        $errors.Add((New-ValidationError -Path $Path -Message "Soubor je podezrele kratky ($($strippedText.Length) znaku, minimum $MinChars)"))
    }

    $inFence = $false
    $lineNumber = 0
    foreach ($line in ($text -split "`r?`n")) {
        $lineNumber++

        if (Test-FenceLine -Line $line) {
            $inFence = -not $inFence
            continue
        }

        if ($inFence) {
            continue
        }

        if ($IncludeTodos -and $TodoPattern.IsMatch($line)) {
            $errors.Add((New-ValidationError -Path $Path -Message "TODO na radku $lineNumber"))
        }

        foreach ($headingError in (Test-Heading -Line $line -LineNumber $lineNumber -Path $Path)) {
            $errors.Add($headingError)
        }

        foreach ($linkError in (Test-Links -Line $line -LineNumber $lineNumber -Path $Path -DocsDirectory $DocsDirectory)) {
            $errors.Add($linkError)
        }
    }

    if ($inFence) {
        $errors.Add((New-ValidationError -Path $Path -Message "Neukonceny blok kodu"))
    }

    return $errors.ToArray()
}

function Test-Docs {
    param(
        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $RootDirectory,

        [Parameter(Mandatory = $true)]
        [System.IO.DirectoryInfo] $DocsDirectory,

        [Parameter(Mandatory = $true)]
        [bool] $IncludeTodos,

        [Parameter(Mandatory = $true)]
        [int] $MinChars
    )

    if ($MinChars -le 0) {
        throw "-MinChars musi byt kladne cislo."
    }

    $errors = New-Object System.Collections.Generic.List[object]
    foreach ($path in (Get-MarkdownFiles -DocsDirectory $DocsDirectory)) {
        foreach ($fileNameError in (Test-FileName -Path $path)) {
            $errors.Add($fileNameError)
        }

        foreach ($markdownError in (Test-MarkdownFile -Path $path -DocsDirectory $DocsDirectory -IncludeTodos $IncludeTodos -MinChars $MinChars)) {
            $errors.Add($markdownError)
        }
    }

    return $errors |
        Sort-Object `
            @{ Expression = { Get-OrdinalSortKey -Value (Get-RelativePosixPath -Path $_.Path -RootDirectory $RootDirectory).ToLowerInvariant() } }, `
            @{ Expression = { Get-OrdinalSortKey -Value $_.Message } }
}

$scriptDirectoryPath = $PSScriptRoot
if ([string]::IsNullOrWhiteSpace($scriptDirectoryPath)) {
    $scriptDirectoryPath = Split-Path -Parent -Path $MyInvocation.MyCommand.Path
}
if ([string]::IsNullOrWhiteSpace($scriptDirectoryPath)) {
    throw "Nelze zjistit adresar skriptu."
}

if ([string]::IsNullOrWhiteSpace($Root)) {
    $Root = (Resolve-Path -LiteralPath (Join-Path -Path $scriptDirectoryPath -ChildPath "..")).Path
}

$rootDirectory = [System.IO.DirectoryInfo]::new((Resolve-Path -LiteralPath $Root).Path)
if (-not $rootDirectory.Exists) {
    throw "Korenovy adresar neexistuje: $($rootDirectory.FullName)"
}

if ([string]::IsNullOrWhiteSpace($DocsRoot)) {
    $resolvedDocsRoot = Join-Path -Path $rootDirectory.FullName -ChildPath $DefaultDocsDir
}
elseif ([System.IO.Path]::IsPathRooted($DocsRoot)) {
    $resolvedDocsRoot = $DocsRoot
}
else {
    $resolvedDocsRoot = Join-Path -Path $rootDirectory.FullName -ChildPath $DocsRoot
}

$docsDirectory = [System.IO.DirectoryInfo]::new((Resolve-Path -LiteralPath $resolvedDocsRoot).Path)
$includeTodos = $Mode -eq "todos"
Write-Output 'Pokud chces zapnout kontrolu TODOs pridej argument "todos": .\tools\md_doc_validator.ps1 todos'
Write-Output "Provadim validaci, chvilku pockej..."

$errors = @(Test-Docs -RootDirectory $rootDirectory -DocsDirectory $docsDirectory -IncludeTodos $includeTodos -MinChars $MinChars)
$relativePaths = @($errors | ForEach-Object { Get-RelativePosixPath -Path $_.Path -RootDirectory $rootDirectory })
$pathWidth = 0
foreach ($relativePath in $relativePaths) {
    if ($relativePath.Length -gt $pathWidth) {
        $pathWidth = $relativePath.Length
    }
}

$numberWidth = $errors.Count.ToString().Length
for ($index = 0; $index -lt $errors.Count; $index++) {
    $number = ($index + 1).ToString().PadLeft($numberWidth)
    $relativePath = $relativePaths[$index].PadRight($pathWidth)
    Write-Output "$number) $relativePath -> $($errors[$index].Message)"
}

if ($errors.Count -gt 0) {
    exit 1
}

exit 0
