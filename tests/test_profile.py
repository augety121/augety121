import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_profile_assets as visuals
import update_profile_data as data


class ProfileTests(unittest.TestCase):
    def test_svg_safety_and_animation(self):
        for path in (ROOT / "assets/profile").glob("*.svg"):
            with self.subTest(path=path.name):
                source = path.read_text(encoding="utf-8")
                root = ET.fromstring(source)
                self.assertIn("viewBox", root.attrib)
                self.assertNotIn("<script", source)
                self.assertNotIn("<foreignObject", source)
                self.assertNotRegex(source, r'(?:href|src)=[\"\']https?://')
        for renderer in (visuals.hero, visuals.project, visuals.footer):
            for lang in ("zh", "en"):
                self.assertIn("@keyframes", renderer(lang, True))
                self.assertIn("prefers-reduced-motion", renderer(lang, True))
                self.assertNotIn("@keyframes", renderer(lang, False))

    def test_local_links_and_languages(self):
        for lang, name in (("zh", "README.md"), ("en", "README.en.md")):
            source = (ROOT / name).read_text(encoding="utf-8")
            for target in re.findall(r'(?:src|srcset|href)="(\./[^"?#]+)"', source):
                self.assertTrue((ROOT / target).is_file(), target)
            for anchor in re.findall(r'href="#([^"]+)"', source):
                self.assertIn(f'id="{anchor}"', source)
            self.assertIn(f'hero-{lang}.svg', source)
            self.assertIn(f'stats-{lang}.svg', source)
        self.assertIn('href="./README.en.md"', (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn('href="./README.md"', (ROOT / "README.en.md").read_text(encoding="utf-8"))

    def test_statistics_localization_and_placeholder(self):
        sample = dict(repositories=102, stars=1234, contributions=88, followers=5, updated="2026-09-08 08:15 UTC+8")
        self.assertIn("公开原创仓库", data.render_stats(sample, "zh"))
        self.assertIn("Public non-fork repos", data.render_stats(sample, "en"))
        self.assertIn("1,234", data.render_stats(sample, "zh"))
        self.assertIn("等待首次", data.render_stats({}, "zh"))
        self.assertIn("—", data.render_stats({}, "zh"))

    def test_repository_pagination(self):
        def page(stars, more, cursor):
            return {"followers": {"totalCount": 5}, "repositories": {"totalCount": 102, "nodes": [{"stargazerCount": s} for s in stars], "pageInfo": {"hasNextPage": more, "endCursor": cursor}}, "contributionsCollection": {"contributionCalendar": {"totalContributions": 88, "weeks": []}}}
        with patch.object(data, "request_page", side_effect=[page([1] * 100, True, "next"), page([3, 4], False, None)]) as request:
            result = data.fetch_profile("test-token", "test-user")
        self.assertEqual(result["stars"], 107)
        self.assertEqual(result["repositories"], 102)
        self.assertEqual(request.call_args_list[1].args[2], "next")

    def test_api_failure_is_not_zero_data(self):
        with patch.object(data, "request_page", side_effect=RuntimeError("API unavailable")):
            with self.assertRaises(RuntimeError):
                data.fetch_profile("test-token", "test-user")

    def test_calendar_and_assets(self):
        sample = {"weeks": [{"contributionDays": [{"date": "2026-09-08", "weekday": 2, "contributionCount": 3}]}]}
        ET.fromstring(data.render_calendar(sample))
        self.assertIn("2026-09-08: 3", data.render_calendar(sample))
        with tempfile.TemporaryDirectory() as directory:
            data.write_assets(sample, Path(directory))
            self.assertEqual(len(list(Path(directory).glob("*.svg"))), 5)
            self.assertFalse((Path(directory) / "contribution-snake.svg").exists())


if __name__ == "__main__":
    unittest.main()
