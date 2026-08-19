import unittest

from daily_update import candidate_score, github_links, render


class DailyUpdateTests(unittest.TestCase):
    def test_github_links_are_unique_and_repository_only(self):
        text = "[A](https://github.com/a/b) [duplicate](https://github.com/a/b/) [issue](https://github.com/a/b/issues)"
        self.assertEqual(github_links(text), [("A", "a/b")])

    def test_report_marks_unverified_entries(self):
        report = render([{"repo": "a/b", "state": "unverified", "error": "404"}], [], __import__("datetime").datetime(2026, 1, 1))
        self.assertIn("unverified", report)
        self.assertIn("404", report)

    def test_candidate_score_rejects_irrelevant_repository(self):
        now = __import__("datetime").datetime(2026, 1, 1, tzinfo=__import__("datetime").timezone.utc)
        score, reasons = candidate_score({"repo": "a/calculator", "description": "math tool"}, now)
        self.assertEqual((score, reasons), (0, ["not relevant"]))


if __name__ == "__main__":
    unittest.main()
