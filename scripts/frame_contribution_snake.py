#!/usr/bin/env python3
"""Frame the real snk SVG without changing its contribution data or animation."""
import math
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from build_profile_assets import OUT, INK, MUTED, svg, text

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def render(source, lang, mobile=False):
    if "<!DOCTYPE" in source.upper() or "<!ENTITY" in source.upper():
        raise ValueError("DTD and entity declarations are not supported")
    root = ET.fromstring(source)
    if root.tag != f"{{{NS}}}svg":
        raise ValueError("Expected an SVG root")
    for node in root.iter():
        name = node.tag.rsplit("}", 1)[-1]
        if name in {"script", "foreignObject"}:
            raise ValueError("Active HTML or scripts are not supported")
        for key, value in node.attrib.items():
            local = key.rsplit("}", 1)[-1]
            if local.lower().startswith("on") or (local in {"href", "src"} and not value.startswith("#")):
                raise ValueError("External resources or event handlers are not supported")
        if name == "style" and re.search(r"@import|url\(\s*['\"]?(?:https?:|//|data:)", node.text or "", re.I):
            raise ValueError("External CSS resources are not supported")
    viewbox = [float(v) for v in root.attrib["viewBox"].replace(",", " ").split()]
    if len(viewbox) != 4 or not all(math.isfinite(v) for v in viewbox) or min(viewbox[2:]) <= 0:
        raise ValueError("Invalid SVG dimensions")
    width = 720 if mobile else 1200
    inner_width = width-56
    inner_height = round(inner_width*viewbox[3]/viewbox[2])
    if inner_height > width:
        raise ValueError("Unexpected contribution graph aspect ratio")
    root.attrib.update(x="28", y="84", width=str(inner_width), height=str(inner_height))
    root.attrib["aria-hidden"] = "true"
    title = "贡献轨迹" if lang == "zh" else "Contribution trail"
    subtitle = "每一次投入，都留下可见的痕迹。" if lang == "zh" else "Small steps. A visible trail."
    body = text(36, 38, title, 27 if mobile else 24, INK, 600)
    body += text(36, 66, subtitle, 21 if mobile else 17, MUTED)
    body += ET.tostring(root, encoding="unicode")
    return svg(body, inner_height+106, title, False, width)


def main():
    source = (OUT / "contribution-snake.svg").read_text(encoding="utf-8")
    # Render every variant before writing, so invalid input never replaces good assets.
    rendered = {f"contribution-{'mobile-' if mobile else ''}{lang}.svg": render(source, lang, mobile) for lang in ("zh", "en") for mobile in (False, True)}
    for filename, content in rendered.items():
        (OUT / filename).write_text(content, encoding="utf-8", newline="\n")
    print("Framed four bilingual contribution animations.")


if __name__ == "__main__":
    main()
