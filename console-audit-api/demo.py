from __future__ import annotations

import json

from analyzer import analyze_console


if __name__ == "__main__":
    sample = """
ReferenceError: tracker is not defined
Failed to load resource: the server responded with a status of 404 ()
Access to fetch at https://api.example.com from origin https://www.example.com was blocked by CORS policy
""".strip()

    print(json.dumps(analyze_console(sample, page_url="https://example.com"), ensure_ascii=False, indent=2))
