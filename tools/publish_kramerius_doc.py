#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_INPUT_PATH = Path("out") / "kramerius-doc.md"
DEFAULT_TIMEOUT_SECONDS = 60


def read_required_env(name: str) -> str:
    value = os.environ.get(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Chybi povinna environment promenna {name}.")
    return value.strip()


def read_documentation(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Soubor s dokumentaci neexistuje: {path}")

    text = path.read_text(encoding="utf-8-sig")
    if not text.strip():
        raise RuntimeError(f"Soubor s dokumentaci je prazdny: {path}")

    return text


def publish_documentation(api_url: str, api_key: str, text: str, timeout_seconds: int) -> dict[str, object]:
    payload = json.dumps({"text": text}).encode("utf-8")
    request = urllib.request.Request(
        api_url,
        data=payload,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "X-API-Key": api_key,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
            response_body = response.read().decode("utf-8")
            status = response.status
    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Upload dokumentace selhal: HTTP {error.code} {error.reason}. Odpoved: {error_body}"
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(f"Upload dokumentace selhal: {error.reason}") from error

    if status < 200 or status >= 300:
        raise RuntimeError(f"Upload dokumentace selhal: HTTP {status}. Odpoved: {response_body}")

    if not response_body.strip():
        return {"status": status}

    parsed_response = json.loads(response_body)
    if not isinstance(parsed_response, dict):
        raise RuntimeError("API vratilo JSON odpoved, ktera neni objekt.")

    return parsed_response


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Odesle vybuildenou Kramerius dokumentaci do kramerius-doc-chat API."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help=f"Cesta k vybuildene dokumentaci. Vychozi hodnota je {DEFAULT_INPUT_PATH}.",
    )
    parser.add_argument(
        "--api-url",
        default=None,
        help="Upload endpoint. Pokud neni zadan, pouzije se env KRAMERIUS_DOC_API_URL.",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="API klic. Pokud neni zadan, pouzije se env KRAMERIUS_DOC_API_KEY.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f"HTTP timeout v sekundach. Vychozi hodnota je {DEFAULT_TIMEOUT_SECONDS}.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.timeout_seconds <= 0:
        raise ValueError("--timeout-seconds musi byt kladne cislo.")

    input_path = args.input.resolve()
    api_url = args.api_url.strip() if args.api_url is not None else read_required_env("KRAMERIUS_DOC_API_URL")
    api_key = args.api_key.strip() if args.api_key is not None else read_required_env("KRAMERIUS_DOC_API_KEY")
    if not api_url:
        raise RuntimeError("Upload endpoint nesmi byt prazdny.")
    if not api_key:
        raise RuntimeError("API klic nesmi byt prazdny.")

    text = read_documentation(input_path)
    response = publish_documentation(api_url, api_key, text, args.timeout_seconds)

    print("Dokumentace byla odeslana.")
    print(json.dumps(response, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
