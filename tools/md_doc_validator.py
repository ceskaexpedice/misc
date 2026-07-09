#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath


DEFAULT_DOCS_DIR = "docs"
DEFAULT_MIN_CHARS = 40
TODO_PATTERN = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
HEADING_PATTERN = re.compile(r"^(?P<indent> {0,3})(?P<marker>#+)(?P<rest>.*)$")
FENCE_PATTERN = re.compile(r"^\s*(```+|~~~+)")
FILE_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
URI_SCHEME_PATTERN = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)


@dataclass(frozen=True)
class ValidationError:
    path: Path
    message: str


def relative_posix_path(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as error:
        raise RuntimeError(f"Cesta neni pod korenem projektu: {path}") from error


def collect_markdown_files(docs_root: Path) -> list[Path]:
    if not docs_root.is_dir():
        raise NotADirectoryError(f"Adresar s dokumentaci neexistuje: {docs_root}")

    files = [path for path in docs_root.rglob("*.md") if path.is_file()]
    files.sort(key=lambda item: item.as_posix().casefold())
    return files


def is_fence_line(line: str) -> bool:
    return FENCE_PATTERN.match(line) is not None


def is_escaped(value: str, index: int) -> bool:
    backslash_count = 0
    cursor = index - 1
    while cursor >= 0 and value[cursor] == "\\":
        backslash_count += 1
        cursor -= 1

    return backslash_count % 2 == 1


def find_closing_paren(value: str, open_paren_index: int) -> int:
    depth = 1
    cursor = open_paren_index + 1

    while cursor < len(value):
        char = value[cursor]
        if char in {"(", ")"} and is_escaped(value, cursor):
            cursor += 1
            continue

        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return cursor

        cursor += 1

    return -1


def iter_markdown_links(line: str) -> list[tuple[str, int]]:
    links: list[tuple[str, int]] = []
    cursor = 0

    while cursor < len(line):
        is_image = line[cursor] == "!" and cursor + 1 < len(line) and line[cursor + 1] == "["
        is_link = line[cursor] == "["
        if not is_image and not is_link:
            cursor += 1
            continue

        start = cursor
        label_start = cursor + 1 if is_image else cursor
        label_end = line.find("]", label_start + 1)
        if label_end == -1:
            break

        if label_end + 1 >= len(line) or line[label_end + 1] != "(":
            cursor = label_end + 1
            continue

        open_paren = label_end + 1
        close_paren = find_closing_paren(line, open_paren)
        if close_paren == -1:
            break

        links.append((line[open_paren + 1 : close_paren], start + 1))
        cursor = close_paren + 1

    return links


def link_destination(raw_target: str) -> str:
    stripped_target = raw_target.strip()
    if not stripped_target:
        return ""

    if stripped_target.startswith("<"):
        end_index = stripped_target.find(">")
        if end_index != -1:
            return stripped_target[1:end_index].strip()

    return stripped_target.split(maxsplit=1)[0]


def is_external_or_anchor_link(target: str) -> bool:
    return (
        target.startswith("#")
        or target.startswith("//")
        or URI_SCHEME_PATTERN.match(target) is not None
    )


def link_path_without_fragment(target: str) -> str:
    return target.split("#", 1)[0].split("?", 1)[0]


def has_link_extension(target_path: str) -> bool:
    suffix = PurePosixPath(target_path.replace("\\", "/")).suffix
    return suffix not in {"", "."}


def has_markdown_extension(target_path: str) -> bool:
    return PurePosixPath(target_path.replace("\\", "/")).suffix.casefold() == ".md"


def has_unsupported_dot_segment(target_path: str) -> bool:
    return any(re.fullmatch(r"\.\.\.+", segment) is not None for segment in target_path.replace("\\", "/").split("/"))


def link_candidate_paths(path: Path, docs_root: Path, target_path: str) -> list[Path]:
    normalized_target = target_path.replace("\\", "/")
    is_absolute = normalized_target.startswith("/")
    relative_target = normalized_target.lstrip("/") if is_absolute else normalized_target
    target_parts = PurePosixPath(relative_target).parts
    base_path = docs_root.joinpath(*target_parts) if is_absolute else path.parent.joinpath(*target_parts)

    if has_link_extension(normalized_target):
        return [base_path]

    candidates = [base_path]
    if not normalized_target.endswith("/"):
        candidates.append(base_path.with_suffix(".md"))
    candidates.append(base_path / "index.md")
    return candidates


def resolve_documentation_link(path: Path, docs_root: Path, target_path: str) -> Path | None:
    if has_unsupported_dot_segment(target_path):
        return None

    resolved_docs_root = docs_root.resolve()

    for candidate in link_candidate_paths(path, docs_root, target_path):
        resolved_candidate = candidate.resolve()
        try:
            resolved_candidate.relative_to(resolved_docs_root)
        except ValueError:
            continue

        if resolved_candidate.is_file():
            return resolved_candidate

    return None


def validate_links(line: str, line_number: int, path: Path, docs_root: Path) -> list[ValidationError]:
    errors: list[ValidationError] = []

    for raw_target, column in iter_markdown_links(line):
        target = link_destination(raw_target)
        if not target:
            errors.append(
                ValidationError(
                    path,
                    f"Rozbity odkaz na radku {line_number}, sloupec {column}: prazdny cil",
                )
            )
            continue

        if is_external_or_anchor_link(target):
            continue

        target_path = link_path_without_fragment(target)
        if not target_path:
            continue

        if has_markdown_extension(target_path):
            errors.append(
                ValidationError(
                    path,
                    f"Podezrely odkaz s priponou .md na radku {line_number}, sloupec {column}",
                )
            )

        resolved_target = resolve_documentation_link(path, docs_root, target_path)
        if resolved_target is None:
            errors.append(
                ValidationError(
                    path,
                    f"Rozbity odkaz na radku {line_number}, sloupec {column}",
                )
            )

    return errors


def validate_file_name(path: Path) -> list[ValidationError]:
    if FILE_NAME_PATTERN.fullmatch(path.name) is not None:
        return []

    return [
        ValidationError(
            path,
            "Neplatne jmeno souboru: pouzij lowercase bez diakritiky a slova oddeluj pomlckou",
        )
    ]


def validate_heading(line: str, line_number: int, path: Path) -> list[ValidationError]:
    match = HEADING_PATTERN.match(line.rstrip("\n\r"))
    if match is None:
        return []

    marker = match.group("marker")
    rest = match.group("rest")
    errors: list[ValidationError] = []

    if len(marker) > 6:
        errors.append(
            ValidationError(
                path,
                f"Chyba v nadpisu na radku {line_number}: nadpis muze mit nejvyse 6 znaku #",
            )
        )
        return errors

    if rest and not rest[0].isspace():
        errors.append(
            ValidationError(
                path,
                f"Chyba v nadpisu na radku {line_number}: chybi mezera za #",
            )
        )
        return errors

    heading_text = rest.strip()
    if not heading_text:
        errors.append(
            ValidationError(
                path,
                f"Chyba v nadpisu na radku {line_number}: chybi text nadpisu",
            )
        )
        return errors

    if heading_text.endswith("#"):
        stripped_closing = heading_text.rstrip("#").rstrip()
        if not stripped_closing:
            errors.append(
                ValidationError(
                    path,
                    f"Chyba v nadpisu na radku {line_number}: chybi text nadpisu",
                )
            )
        elif not re.search(r"\s#+$", heading_text):
            errors.append(
                ValidationError(
                    path,
                    f"Chyba v nadpisu na radku {line_number}: neplatne ukonceni nadpisu znakem #",
                )
            )

    return errors


def validate_markdown_file(path: Path, docs_root: Path, min_chars: int, include_todos: bool) -> list[ValidationError]:
    text = path.read_text(encoding="utf-8-sig")
    stripped_text = text.strip()
    errors: list[ValidationError] = []

    if not stripped_text:
        errors.append(ValidationError(path, "Soubor je prazdny"))
        return errors

    if len(stripped_text) < min_chars:
        errors.append(
            ValidationError(
                path,
                f"Soubor je podezrele kratky ({len(stripped_text)} znaku, minimum {min_chars})",
            )
        )

    in_fence = False
    for line_number, line in enumerate(text.splitlines(), start=1):
        if is_fence_line(line):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        if include_todos and TODO_PATTERN.search(line):
            errors.append(ValidationError(path, f"TODO na radku {line_number}"))

        errors.extend(validate_heading(line, line_number, path))
        errors.extend(validate_links(line, line_number, path, docs_root))

    if in_fence:
        errors.append(ValidationError(path, "Neukonceny blok kodu"))

    return errors


def validate_docs(root: Path, docs_root: Path, min_chars: int, include_todos: bool) -> list[ValidationError]:
    if min_chars <= 0:
        raise ValueError("--min-chars musi byt kladne cislo.")

    errors: list[ValidationError] = []
    for path in collect_markdown_files(docs_root):
        errors.extend(validate_file_name(path))
        errors.extend(validate_markdown_file(path, docs_root, min_chars, include_todos))

    errors.sort(key=lambda item: (relative_posix_path(item.path, root).casefold(), item.message))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validuje markdown dokumentaci pro Kramerius.")
    parser.add_argument(
        "mode",
        nargs="?",
        choices=("todos",),
        help="Zapne kontrolu TODO/TBD/FIXME markeru.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Korenovy adresar projektu. Vychozi hodnota je nadrazeny adresar slozky tools.",
    )
    parser.add_argument(
        "--docs-root",
        type=Path,
        default=None,
        help=f"Adresar s markdown dokumentaci. Vychozi hodnota je {DEFAULT_DOCS_DIR} v koreni projektu.",
    )
    parser.add_argument(
        "--min-chars",
        type=int,
        default=DEFAULT_MIN_CHARS,
        help=f"Minimalni pocet znaku po orezu bilych znaku. Vychozi hodnota je {DEFAULT_MIN_CHARS}.",
    )
    return parser.parse_args()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Korenovy adresar neexistuje: {root}")

    docs_root = args.docs_root if args.docs_root is not None else root / DEFAULT_DOCS_DIR
    if not docs_root.is_absolute():
        docs_root = root / docs_root
    docs_root = docs_root.resolve()

    print('Pokud chces zapnout kontrolu TODOs pridej argument "todos": python .\\tools\\md_doc_validator.py todos', flush=True)
    print("Provadim validaci, chvilku pockej...", flush=True)

    errors = validate_docs(root, docs_root, args.min_chars, args.mode == "todos")
    relative_paths = [relative_posix_path(error.path, root) for error in errors]
    path_width = max((len(path) for path in relative_paths), default=0)
    number_width = len(str(len(errors)))

    for index, (error, relative_path) in enumerate(zip(errors, relative_paths), start=1):
        print(f"{index:{number_width}d}) {relative_path:<{path_width}} -> {error.message}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
