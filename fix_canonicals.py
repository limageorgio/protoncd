import glob
import os
import re


ROOT = "https://www.protoncd.com.br/"
TARGET_GLOBS = [
    "artigos/elevadores/*.html",
    "artigos/playgrounds/*.html",
]


def expected_url(path: str) -> str:
    rel = path.replace("\\", "/")
    if rel.endswith("index.html"):
        return ROOT + rel.replace("index.html", "")
    return ROOT + rel


def canonical_pattern() -> re.Pattern:
    return re.compile(
        r"(<link\b[^>]*\brel=[\"']canonical[\"'][^>]*\bhref=[\"'])([^\"']+)([\"'][^>]*>)",
        re.IGNORECASE,
    )


def fix_file(path: str) -> tuple[bool, str | None, str | None]:
    with open(path, "r", encoding="utf-8") as fh:
        content = fh.read()

    p = canonical_pattern()
    m = p.search(content)
    if not m:
        return False, None, None

    current = m.group(2)
    expected = expected_url(path)
    if current == expected:
        return False, current, expected

    # Replace the canonical URL everywhere in the file so linked SEO fields
    # (alternate/hreflang, og:url and JSON-LD @id) stay consistent.
    updated = content.replace(current, expected)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(updated)
    return True, current, expected


def main() -> None:
    files: list[str] = []
    for pattern in TARGET_GLOBS:
        files.extend(glob.glob(pattern))

    files = sorted(f for f in files if os.path.isfile(f))
    total = len(files)
    fixed = 0

    for path in files:
        changed, current, expected = fix_file(path)
        if changed:
            fixed += 1
            print(f"FIXED: {path}")
            print(f"  FROM: {current}")
            print(f"  TO:   {expected}")

    print(f"TOTAL_FILES={total}")
    print(f"TOTAL_FIXED={fixed}")


if __name__ == "__main__":
    main()
