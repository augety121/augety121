#!/usr/bin/env python3
"""Build bilingual animated SVGs using only the Python standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "profile"
INK, MUTED, BLUE, MINT = "#243B53", "#607D8B", "#438BC5", "#309F8B"


def text(x, y, value, size=18, color=INK, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'


def svg(body, height, title, animated=True, width=1200):
    animation = """
      .flow{stroke-dasharray:14 180;animation:flow 7s linear infinite}
      .flow-slow{stroke-dasharray:10 240;animation:flowSlow 11s linear infinite reverse}
      .float{animation:float 8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
      .breathe{animation:breathe 5s ease-in-out infinite}
      @keyframes flow{to{stroke-dashoffset:-776}}
      @keyframes flowSlow{to{stroke-dashoffset:-1000}}
      @keyframes float{50%{transform:translateY(-9px)}}
      @keyframes breathe{50%{opacity:.45}}
      @media(prefers-reduced-motion:reduce){*{animation:none!important}}
    """ if animated else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title, quote=True)}">
<title>{escape(title)}</title>
<defs>
  <linearGradient id="paper" x2="1" y2="1"><stop stop-color="#F6FBFF"/><stop offset=".55" stop-color="#F3FAFB"/><stop offset="1" stop-color="#EBF8F0"/></linearGradient>
  <linearGradient id="accent"><stop stop-color="#69AFDD"/><stop offset="1" stop-color="#68C4AC"/></linearGradient>
  <radialGradient id="glow"><stop stop-color="#A9D9EF" stop-opacity=".38"/><stop offset="1" stop-color="#A9D9EF" stop-opacity="0"/></radialGradient>
  <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#A3BCC8" opacity=".23"/></pattern>
  <clipPath id="clip"><rect x="1" y="1" width="{width-2}" height="{height-2}" rx="28"/></clipPath>
  <style>text{{font-family:'Segoe UI','Microsoft YaHei','PingFang SC','Noto Sans CJK SC',sans-serif}}.flow{{stroke-dasharray:14 180}}.flow-slow{{stroke-dasharray:10 240}}{animation}</style>
</defs>
<g clip-path="url(#clip)"><rect width="{width}" height="{height}" fill="url(#paper)"/>{body}</g>
<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="28" fill="none" stroke="#DDEBEA"/>
</svg>\n'''


def hero(lang, animated):
    zh = lang == "zh"
    body = '<rect x="640" width="560" height="440" fill="url(#dots)"/><circle cx="938" cy="195" r="275" fill="url(#glow)"/>'
    body += '<rect x="52" y="43" width="28" height="4" rx="2" fill="url(#accent)"/>'
    body += text(94, 51, "开发者 / 开源实践" if zh else "DEVELOPER / OPEN SOURCE", 15, MUTED, 600, 'letter-spacing="2"')
    body += text(52, 139, "构建可靠的" if zh else "Building reliable", 55 if zh else 50, INK, 700)
    body += text(52, 209, "Agent 系统。" if zh else "agent systems.", 62 if zh else 58, BLUE, 750)
    body += text(54, 266, "以证据为起点，让每一次行动都可以被验证。" if zh else "Grounded in evidence. Built for verifiable action.", 21 if zh else 19, MUTED)
    body += text(54, 311, "检索增强 / 上下文工程 / MCP / 可复现评测" if zh else "RAG / Context engineering / MCP / Evaluation", 17, MUTED)
    body += '<path d="M54 362 H585" stroke="#CFE1E5"/>'
    body += text(54, 397, "持续学习，认真构建。" if zh else "Learning in public. Building with care.", 16, MUTED)
    routes = [("M670 105 C735 105 731 193 824 193 S930 77 1108 77", BLUE), ("M663 264 C750 264 725 193 824 193 S949 326 1138 326", MINT), ("M690 357 C779 357 725 242 839 242 S955 174 1138 174", "#8CBBD4")]
    for i, (path, color) in enumerate(routes):
        body += f'<path d="{path}" fill="none" stroke="{color}" stroke-width="20" opacity=".08"/><path d="{path}" fill="none" stroke="{color}" stroke-width="1.4" opacity=".35"/><path class="flow" style="animation-delay:-{i*2}s" d="{path}" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round"/>'
    nodes = [(710,107,"证据" if zh else "EVIDENCE","01",BLUE),(876,194,"上下文" if zh else "CONTEXT","02",BLUE),(1052,174,"工具" if zh else "TOOLS","03",MINT),(1051,326,"验证" if zh else "VERIFY","04",MINT)]
    for x, y, label, idx, color in nodes:
        body += f'<g class="float" style="animation-delay:-{int(idx)}s"><rect x="{x-57}" y="{y-33}" width="114" height="66" rx="18" fill="#FFFFFF" stroke="#D8E9EA"/>'
        body += text(x, y-9, idx, 12, color, 600, 'text-anchor="middle" letter-spacing="2"')
        body += text(x, y+16, label, 18 if zh else 14, INK, 600, 'text-anchor="middle"') + '</g>'
    body += '<circle class="breathe" cx="816" cy="357" r="5" fill="#77BFAE"/><circle cx="1164" cy="50" r="4" fill="#A4CBE2"/>'
    return svg(body, 440, "构建可靠的 Agent 系统" if zh else "Building reliable agent systems", animated)


def project(lang, animated):
    zh = lang == "zh"
    body = text(44, 43, "正在探索 / 精选开源" if zh else "IN FOCUS / OPEN SOURCE", 14, MUTED, 600, 'letter-spacing="2"')
    body += text(44, 99, "MCP State Twin", 39, INK, 700)
    body += text(44, 140, "同一起点，不同路径，可比较的最终状态。" if zh else "Same start. Different paths. Comparable outcomes.", 20 if zh else 17, MUTED)
    body += '<rect x="44" y="168" width="110" height="29" rx="14" fill="#DCEFE8"/>'
    body += text(99, 188, "开发预览" if zh else "PREVIEW", 13, "#397565", 600, 'text-anchor="middle"')
    body += text(174, 188, "Go · MCP · 评测环境" if zh else "Go · MCP · Evaluation", 15, MUTED)
    body += '<path d="M700 116 C786 116 762 64 839 64 H1119 M700 116 C786 116 762 174 839 174 H1119" fill="none" stroke="#CBDFE5" stroke-width="2"/>'
    body += '<path class="flow" d="M700 116 C786 116 762 64 839 64 H1119" fill="none" stroke="#4A94C8" stroke-width="4" stroke-linecap="round"/><path class="flow-slow" d="M700 116 C786 116 762 174 839 174 H1119" fill="none" stroke="#4CAC96" stroke-width="4" stroke-linecap="round"/>'
    for x, y, label, color in [(693,116,"快照" if zh else "Snapshot",BLUE),(894,64,"运行 A" if zh else "Run A",BLUE),(894,174,"运行 B" if zh else "Run B",MINT)]:
        body += f'<circle cx="{x}" cy="{y}" r="27" fill="#FFFFFF" stroke="#D5E6E9"/><circle class="breathe" cx="{x}" cy="{y}" r="8" fill="{color}"/>'
        body += text(x+40, y+6, label, 16, INK, 500)
    body += text(1127, 122, "比较" if zh else "Diff", 15, MUTED, 500, 'text-anchor="middle"')
    return svg(body, 235, "MCP State Twin · " + ("开发预览" if zh else "Development preview"), animated)


def footer(lang, animated):
    body = '<path d="M0 78 Q180 -12 380 65 T790 56 T1230 46" fill="none" stroke="#BEDDDF" stroke-width="1.5"/><path class="flow-slow" d="M0 78 Q180 -12 380 65 T790 56 T1230 46" fill="none" stroke="#64ACAA" stroke-width="3"/><rect x="421" y="29" width="358" height="50" rx="25" fill="#F4FAFA"/>'
    body += text(600, 60, "保持好奇，持续构建。" if lang == "zh" else "Stay curious. Keep building.", 21, MUTED, 500, 'text-anchor="middle"')
    return svg(body, 105, "保持好奇，持续构建" if lang == "zh" else "Stay curious. Keep building.", animated)


def hero_mobile(lang, animated):
    zh = lang == "zh"
    body = text(42, 45, "开发者 / 开源实践" if zh else "DEVELOPER / OPEN SOURCE", 18, MUTED, 600)
    body += text(42, 121, "构建可靠的" if zh else "Building reliable", 50, INK, 700)
    body += text(42, 195, "Agent 系统。" if zh else "agent systems.", 61, BLUE, 750)
    body += text(44, 250, "以证据为起点，" if zh else "Grounded in evidence.", 25, MUTED)
    body += text(44, 287, "让每一次行动都可以被验证。" if zh else "Built for verifiable action.", 25, MUTED)
    path = "M55 380 C158 320 199 440 304 380 S466 320 570 380 S680 405 710 365"
    body += f'<path d="{path}" fill="none" stroke="#D2E7E9" stroke-width="12"/><path class="flow" d="{path}" fill="none" stroke="#63ADBF" stroke-width="4"/>'
    for x, label in [(110,"证据" if zh else "Evidence"),(280,"上下文" if zh else "Context"),(450,"工具" if zh else "Tools"),(620,"验证" if zh else "Verify")]:
        body += f'<rect x="{x-65}" y="355" width="130" height="55" rx="18" fill="#FFFFFF" stroke="#D8E9EA"/>'
        body += text(x, 390, label, 21, INK, 600, 'text-anchor="middle"')
    body += text(44, 478, "持续学习，认真构建。" if zh else "Learning in public. Building with care.", 20, MUTED)
    return svg(body, 515, "构建可靠的 Agent 系统" if zh else "Building reliable agent systems", animated, 720)


def project_mobile(lang, animated):
    zh = lang == "zh"
    body = text(36, 40, "正在探索 / 精选开源" if zh else "IN FOCUS / OPEN SOURCE", 18, MUTED, 600)
    body += text(36, 105, "MCP State Twin", 46, INK, 700)
    body += text(36, 153, "同一起点，不同路径，可比较的最终状态。" if zh else "Same start. Different paths. Comparable outcomes.", 24 if zh else 22, MUTED)
    body += text(36, 198, "开发预览 · Go · MCP · 评测环境" if zh else "Development preview · Go · MCP · Evaluation", 20, MINT, 500)
    body += '<path d="M36 231 H684" stroke="#D0E4E6"/><path class="flow" d="M36 231 H684" stroke="#63ADBF" stroke-width="3"/>'
    return svg(body, 260, "MCP State Twin", animated, 720)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lang in ("zh", "en"):
        for name, renderer in (("hero", hero), ("project", project), ("footer", footer), ("hero-mobile", hero_mobile), ("project-mobile", project_mobile)):
            for animated in (True, False):
                suffix = "" if animated else "-static"
                (OUT / f"{name}-{lang}{suffix}.svg").write_text(renderer(lang, animated), encoding="utf-8", newline="\n")
    print("Generated 20 bilingual desktop/mobile profile assets.")


if __name__ == "__main__":
    main()
