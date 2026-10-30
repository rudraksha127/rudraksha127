"""Unit tests for the profile README validator."""

import unittest

from validate_profile import collect_anchors, find_placeholders, strip_fenced_code


class ProfileValidatorTests(unittest.TestCase):
    def test_headings_inside_backtick_fences_do_not_create_anchors(self) -> None:
        fence = chr(96) * 3
        markdown = "# Real heading\n" + fence + "markdown\n## Fake heading\n" + fence + "\n"
        anchors = collect_anchors(markdown)
        self.assertIn("real-heading", anchors)
        self.assertNotIn("fake-heading", anchors)

    def test_headings_inside_tilde_fences_do_not_create_anchors(self) -> None:
        markdown = "## Visible\n~~~md\n### Hidden section\n~~~\n"
        anchors = collect_anchors(markdown)
        self.assertIn("visible", anchors)
        self.assertNotIn("hidden-section", anchors)

    def test_duplicate_visible_headings_get_distinct_anchors(self) -> None:
        markdown = "## Overview\n## Overview\n"
        self.assertEqual(collect_anchors(markdown), {"overview", "overview-1"})

    def test_code_fence_contents_are_removed(self) -> None:
        fence = chr(96) * 3
        markdown = "before\n" + fence + "text\nTODO\n[Your Name]\n" + fence + "\nafter"
        cleaned = strip_fenced_code(markdown)
        self.assertIn("before", cleaned)
        self.assertIn("after", cleaned)
        self.assertNotIn("TODO", cleaned)

    def test_common_placeholders_are_detected(self) -> None:
        markdown = (
            "TODO: add project\n"
            "[Your Name]\n"
            "https://example.com/demo\n"
            "YOUR_API_URL\n"
            "https://your-deployed-instance.vercel.app\n"
        )
        found = find_placeholders(markdown)
        self.assertGreaterEqual(len(found), 5)

    def test_empty_links_are_detected(self) -> None:
        self.assertTrue(find_placeholders('[Open](#) <a href="#">link</a>'))

    def test_normal_content_has_no_placeholders(self) -> None:
        markdown = (
            "# Engineering profile\n"
            "Projects, source code, and verified evidence.\n"
            "https://github.com/rudraksha127\n"
        )
        self.assertEqual(find_placeholders(markdown), [])


if __name__ == "__main__":
    unittest.main()
