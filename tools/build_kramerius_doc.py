#!/usr/bin/env python3

# python .\tools\build_kramerius_doc.py
# output: .\out\kramerius-doc.md

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path


DEFAULT_OUTPUT_NAME = "kramerius-doc.md"
DEFAULT_OUTPUT_DIR = "out"
INDEX_SEARCH_SECTION_HEADING = "## 🔍 Hledání v dokumentaci"

DOCS_SECTION_ORDER = {
    "getting-started": 10,
    "core-concepts": 20,
    "domain-concepts": 30,
    "architecture": 40,
    "configuration": 50,
    "deployment": 60,
    "guides": 70,
    "scenarios": 80,
    "reference": 90,
}

SECTION_CHILD_ORDER = {
    ("getting-started",): {
        "index.md": 0,
        "curator.md": 10,
        "admin.md": 20,
        "developer.md": 30,
    },
    ("guides",): {
        "index.md": 0,
        "curator": 10,
        "admin": 20,
        "developer": 30,
    },
    ("reference",): {
        "index.md": 0,
        "security": 10,
    },
    ("reference", "security"): {
        "index.md": 0,
        "authentication": 10,
        "authorization": 20,
        "actions": 30,
        "criteria": 40,
        "data-model": 50,
        "api.md": 60,
    },
}


def natural_key(value: str) -> tuple[object, ...]:
    parts = re.split(r"(\d+)", value.casefold())
    return tuple(int(part) if part.isdigit() else part for part in parts)


def markdown_sort_key(path: Path, docs_root: Path) -> tuple[object, ...]:
    relative = path.relative_to(docs_root)
    lower_parts = tuple(part.casefold() for part in relative.parts)

    if lower_parts == ("index.md",):
        return (0,)

    if len(lower_parts) == 1:
        return (950, path_components_key(lower_parts))

    section = lower_parts[0]
    section_order = DOCS_SECTION_ORDER.get(section, 900)
    return (
        section_order,
        section_child_order_key(lower_parts),
        path_components_key(lower_parts[1:]),
    )


def section_child_order_key(parts: tuple[str, ...]) -> tuple[int, str]:
    matched_prefix: tuple[str, ...] | None = None
    matched_child_order: dict[str, int] | None = None

    for prefix, child_order in SECTION_CHILD_ORDER.items():
        if parts[: len(prefix)] != prefix:
            continue

        if matched_prefix is None or len(prefix) > len(matched_prefix):
            matched_prefix = prefix
            matched_child_order = child_order

    if matched_prefix is None or matched_child_order is None:
        return (900, "")

    if len(parts) == len(matched_prefix):
        return (0, "")

    child = parts[len(matched_prefix)]
    return (matched_child_order.get(child, 900), child)



def path_components_key(parts: tuple[str, ...]) -> tuple[object, ...]:
    key: list[object] = []

    for index, part in enumerate(parts):
        is_last = index == len(parts) - 1
        if is_last and part in {"index.md", "readme.md"}:
            priority = 0
        elif is_last:
            priority = 1
        else:
            priority = 2

        key.append((priority, natural_key(part)))

    return tuple(key)


def collect_markdown_files(docs_root: Path, output_path: Path) -> list[Path]:
    files: list[Path] = []
    resolved_output = output_path.resolve()

    for path in docs_root.rglob("*.md"):
        if not path.is_file():
            continue

        if path.resolve() == resolved_output:
            continue

        files.append(path)

    files.sort(key=lambda item: markdown_sort_key(item, docs_root))
    return files


def remove_index_search_section(text: str) -> str:
    section_start = text.find(INDEX_SEARCH_SECTION_HEADING)
    if section_start == -1:
        return text

    section_end_match = re.search(r"^---\s*$", text[section_start:], flags=re.MULTILINE)
    if section_end_match is None:
        raise ValueError(
            f"Sekce '{INDEX_SEARCH_SECTION_HEADING}' nema ukoncovaci oddelovac '---'."
        )

    section_end = section_start + section_end_match.end()
    return text[:section_start].rstrip() + "\n\n" + text[section_end:].lstrip()


def read_non_empty_text(path: Path, docs_root: Path) -> str | None:
    text = path.read_text(encoding="utf-8-sig")
    if path.relative_to(docs_root).as_posix() == "index.md":
        text = remove_index_search_section(text)

    if not text.strip():
        return None

    return text.strip()


def format_generated_at(value: str | None) -> str:
    if value is None:
        return datetime.now().astimezone().isoformat(timespec="seconds")

    parsed_value = value.strip()
    if not parsed_value:
        raise ValueError("Cas generovani nesmi byt prazdny.")

    if parsed_value.endswith("Z"):
        parsed_value = parsed_value[:-1] + "+00:00"

    parsed_datetime = datetime.fromisoformat(parsed_value)
    if parsed_datetime.tzinfo is None:
        parsed_datetime = parsed_datetime.astimezone()

    return parsed_datetime.isoformat(timespec="seconds")


def build_document(root: Path, output_path: Path, generated_at: str | None) -> tuple[int, int]:
    docs_root = root / "docs"
    if not docs_root.is_dir():
        raise NotADirectoryError(f"Adresar s dokumentaci neexistuje: {docs_root}")

    markdown_files = collect_markdown_files(docs_root, output_path)
    if not markdown_files:
        raise RuntimeError(f"Nebyly nalezeny zadne markdown soubory v {docs_root}.")

    included_count = 0
    skipped_empty_count = 0
    chunks: list[str] = [f"Build date: {format_generated_at(generated_at)}", ""]

    for path in markdown_files:
        text = read_non_empty_text(path, docs_root)
        if text is None:
            skipped_empty_count += 1
            continue

        relative_path = path.relative_to(docs_root).as_posix()
        chunks.append(f"=== {relative_path} ===")
        chunks.append("")
        chunks.append(text)
        chunks.append("")
        included_count += 1

    if included_count == 0:
        raise RuntimeError("Vsechny nalezene markdown soubory jsou prazdne.")

    output_path.write_text("\n".join(chunks).rstrip() + "\n", encoding="utf-8")
    return included_count, skipped_empty_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Slouci markdown dokumentaci Krameria do jednoho souboru."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="Korenovy adresar projektu. Vychozi hodnota je nadrazeny adresar slozky tools.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=f"Vystupni soubor. Vychozi hodnota je {DEFAULT_OUTPUT_DIR}/{DEFAULT_OUTPUT_NAME} v koreni projektu.",
    )
    parser.add_argument(
        "--generated-at",
        default=None,
        help="Cas generovani ve formatu ISO 8601. Bez hodnoty se pouzije aktualni lokalni cas.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"Korenovy adresar neexistuje: {root}")

    output_path = args.output if args.output is not None else root / DEFAULT_OUTPUT_DIR / DEFAULT_OUTPUT_NAME
    if not output_path.is_absolute():
        output_path = root / output_path
    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    included_count, skipped_empty_count = build_document(root, output_path, args.generated_at)
    print(f"Vytvoreno: {output_path}")
    print(f"Zahrnuto markdown souboru: {included_count}")
    print(f"Preskoceno prazdnych souboru: {skipped_empty_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
