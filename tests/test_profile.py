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
import frame_contribution_snake as snake_frame


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
        for renderer in (visuals.hero, visuals.hero_mobile, visuals.project, visuals.project_mobile, visuals.footer, visuals.craft, visuals.craft_mobile, visuals.focus, visuals.focus_mobile):
            for lang in ("zh", "en"):
                self.assertIn("@keyframes", renderer(lang, True))
                self.assertIn("prefers-reduced-motion", renderer(lang, True))
                self.assertNotIn("@keyframes", renderer(lang, False))

    def test_hero_has_no_numbered_labels(self):
        for renderer in (visuals.hero, visuals.hero_mobile):
            for lang in ("zh", "en"):
                for animated in (True, False):
                    root = ET.fromstring(renderer(lang, animated))
                    labels = [e.text for e in root.findall(".//{http://www.w3.org/2000/svg}text")]
                    self.assertFalse(any(label in {"01", "02", "03", "04"} for label in labels))

    def test_craft_has_direction_indicators(self):
        for mobile in (False, True):
            root = ET.fromstring(visuals.craft("zh", True, mobile))
            arrows = [e for e in root.iter() if e.attrib.get("class") == "craft-arrow"]
            self.assertEqual(len(arrows), 4)

    def test_contribution_frame_preserves_animation(self):
        source = (ROOT / "assets/profile/contribution-snake.svg").read_text(encoding="utf-8")
        original = ET.fromstring(source)
        ns = {"s": "http://www.w3.org/2000/svg"}
        for lang in ("zh", "en"):
            for mobile in (False, True):
                rendered = ET.fromstring(snake_frame.render(source, lang, mobile))
                nested = rendered.find(".//s:svg", ns)
                self.assertEqual(original.attrib["viewBox"], nested.attrib["viewBox"])
                self.assertEqual([ET.tostring(e) for e in original], [ET.tostring(e) for e in nested])
                self.assertEqual(rendered.attrib["width"], "720" if mobile else "1200")

    def test_contribution_frame_rejects_unsafe_input(self):
        prefix = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 192">'
        for content in ('<script/>', '<image href="https://example.com/a.svg"/>', '<g onload="run()"/>', '<style>@import url(https://example.com/a.css)</style>'):
            with self.assertRaises(ValueError):
                snake_frame.render(prefix+content+'</svg>', "zh")

    def test_focus_and_contribution_locales(self):
        for lang, filename in (("zh", "README.md"), ("en", "README.en.md")):
            source = (ROOT / filename).read_text(encoding="utf-8")
            for asset in (f"focus-{lang}.svg", f"focus-mobile-{lang}.svg", f"contribution-{lang}.svg", f"contribution-mobile-{lang}.svg"):
                self.assertIn(asset, source)
            self.assertIn('href="#top"', source)

    def test_new_section_and_responsive_assets(self):
        for lang, filename in (("zh", "README.md"), ("en", "README.en.md")):
            source = (ROOT / filename).read_text(encoding="utf-8")
            self.assertIn('href="#craft"', source)
            self.assertIn('id="craft"', source)
            for suffix in (f"craft-{lang}.svg", f"craft-{lang}-static.svg", f"craft-mobile-{lang}.svg", f"craft-mobile-{lang}-static.svg"):
                self.assertIn(suffix, source)

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
