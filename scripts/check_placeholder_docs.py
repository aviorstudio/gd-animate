#!/usr/bin/env python3
"""Verify that gd-animate remains a truthfully documented placeholder."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REQUIRED_TEXT = (
    "## Status: retained placeholder",
    "does not currently contain a Godot addon",
    "public API, installable package, or release",
    "There is no supported integration or version for consumers to adopt.",
    "fieldsofrevik/issues/141",
)
ADDON_OR_PACKAGE_PATHS = (
    ROOT / "addon",
    ROOT / "addons",
    ROOT / "gdam.json",
    ROOT / "plugin.cfg",
)


def main() -> int:
    readme = README.read_text(encoding="utf-8")
    failures = [f"README is missing: {text!r}" for text in REQUIRED_TEXT if text not in readme]
    failures.extend(
        f"placeholder repository unexpectedly contains {path.relative_to(ROOT)}"
        for path in ADDON_OR_PACKAGE_PATHS
        if path.exists()
    )

    assertion_count = len(REQUIRED_TEXT) + len(ADDON_OR_PACKAGE_PATHS)
    print(f"PLACEHOLDER_DOCS_ASSERTIONS_REACHED={assertion_count}")
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("Placeholder documentation check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
