from __future__ import annotations

import unittest

from analyzer import analyze_console


class AnalyzerTest(unittest.TestCase):
    def test_detects_reference_error(self) -> None:
        result = analyze_console("ReferenceError: foo is not defined")
        self.assertEqual(result["finding_count"], 1)
        self.assertEqual(result["highest_severity"], "high")
        self.assertIn("javascript-runtime", result["summary"])

    def test_detects_cors(self) -> None:
        result = analyze_console("Access to fetch at https://api.example.com from origin https://site.example was blocked by CORS policy")
        self.assertEqual(result["finding_count"], 1)
        self.assertEqual(result["findings"][0]["category"], "network-policy")

    def test_ignores_clean_input(self) -> None:
        result = analyze_console("Console initialized successfully")
        self.assertEqual(result["finding_count"], 0)
        self.assertEqual(result["summary"], "Nenhum erro reconhecido automaticamente.")


if __name__ == "__main__":
    unittest.main()
