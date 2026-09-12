#!/usr/bin/env python3
"""Build bilingual animated SVGs using only the Python standard library."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "profile"
INK, MUTED, BLUE, MINT = "#243B53", "#607D8B", "#438BC5", "#309F8B"


def text(x, y, value, size=18, color=INK, weight=400, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(str(value))}</text>'


def svg(body, height, title, animated=True, width=1200, framed=True):
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
<g clip-path="url(#clip)"><rect width="{width}" height="{height}" fill="{'url(#paper)' if framed else 'none'}"/>{body}</g>
<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="28" fill="none" stroke="{'#DDEBEA' if framed else 'none'}"/>
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
    nodes = [(710,107,"证据" if zh else "EVIDENCE"),(876,194,"上下文" if zh else "CONTEXT"),(1052,174,"工具" if zh else "TOOLS"),(1051,326,"验证" if zh else "VERIFY")]
    for delay, (x, y, label) in enumerate(nodes, 1):
        body += f'<g class="float" style="animation-delay:-{delay}s"><rect x="{x-57}" y="{y-29}" width="114" height="58" rx="18" fill="#FFFFFF" stroke="#D8E9EA"/>'
        body += text(x, y+7, label, 20 if zh else 15, INK, 600, 'text-anchor="middle"') + '</g>'
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
    for route, color in [("M766 121 C797 121 795 74 826 74 M960 74 C1005 74 1006 127 1050 127", BLUE), ("M766 121 C797 121 795 190 826 190 M960 190 C1005 190 1006 127 1050 127", MINT)]:
        body += f'<path d="{route}" fill="none" stroke="#C7E0E4" stroke-width="2"/><path class="flow" d="{route}" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round"/>'
    for x, y, w, label, color in [(656,90,110,"快照" if zh else "Snapshot",BLUE),(826,47,134,"运行 A" if zh else "Run A",BLUE),(826,163,134,"运行 B" if zh else "Run B",MINT),(1050,100,104,"比较终态" if zh else "Compare",MINT)]:
        body += f'<rect x="{x}" y="{y}" width="{w}" height="54" rx="17" fill="#FFFFFF" stroke="#D5E6E9"/>'
        body += text(x+w/2, y+34, label, 17 if zh else 16, color, 600, 'text-anchor="middle"')
    body += text(711, 175, "相同起点" if zh else "Same start", 14, MUTED, 400, 'text-anchor="middle"')
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


def craft(lang, animated, mobile=False):
    zh = lang == "zh"
    title = "把问题变成可验证的进展" if zh else "Turn questions into verifiable progress"
    body = text(36, 44, title, 24 if mobile else 26, INK, 600)
    labels = [("拆解问题", "明确目标与边界"), ("小步实现", "做出最小完整闭环"), ("证据验证", "用测试与轨迹检查结果"), ("复盘迭代", "把经验沉淀为下一步")] if zh else [("Define", "Goals and boundaries"), ("Build", "A small, complete loop"), ("Verify", "Tests, traces and results"), ("Iterate", "Learn and improve")]
    if mobile:
        positions = [(36, 80), (384, 80), (384, 234), (36, 234)]
        width, height, card_width = 720, 398, 300
        path = "M336 138 H384 M534 196 V234 M384 292 H336 M186 234 V196"
        arrows = ["M358 133 L366 138 L358 143", "M529 211 L534 219 L539 211", "M362 287 L354 292 L362 297", "M181 219 L186 211 L191 219"]
    else:
        positions = [(36 + i * 288, 83) for i in range(4)]
        width, height, card_width = 1200, 260, 264
        path = "M300 141 H324 M588 141 H612 M876 141 H900 M1032 199 V221 H168 V199"
        arrows = ["M307 136 L315 141 L307 146", "M595 136 L603 141 L595 146", "M883 136 L891 141 L883 146", "M614 216 L606 221 L614 226"]
    body += f'<path d="{path}" fill="none" stroke="#C2DFE3" stroke-width="2"/><path class="flow" d="{path}" fill="none" stroke="#59AAA9" stroke-width="3"/>'
    for arrow in arrows:
        body += f'<path class="craft-arrow" d="{arrow}" fill="none" stroke="#69AAA9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
    for i, ((x, y), (label, description)) in enumerate(zip(positions, labels)):
        color = BLUE if i < 2 else MINT
        body += f'<rect x="{x}" y="{y}" width="{card_width}" height="116" rx="18" fill="#FFFFFF" fill-opacity=".88" stroke="#D8E9EA"/>'
        body += f'<rect x="{x+22}" y="{y+24}" width="4" height="25" rx="2" fill="{color}"/>'
        body += text(x+40, y+45, label, 26 if mobile else 24, INK, 600)
        body += text(x+22, y+86, description, 20 if mobile else 17, MUTED)
    caption = "保持反馈，让每次迭代都有依据。" if zh else "Keep the feedback loop open."
    body += text(width/2, height-19, caption, 17 if mobile else 15, MUTED, 400, 'text-anchor="middle"')
    return svg(body, height, title, animated, width)


def craft_mobile(lang, animated):
    return craft(lang, animated, mobile=True)


def focus(lang, animated, mobile=False):
    zh = lang == "zh"
    topics = [("上下文工程", "检索 · 重排 · 知识图谱", "让有用的信息进入上下文"), ("工具运行时", "MCP · 状态 · 故障恢复", "让每一步行动有边界"), ("可靠评测", "追踪 · 断言 · 可复现性", "让改进有证据可循")] if zh else [("Context", "Retrieval · Reranking · Graphs", "Bring useful evidence into context"), ("Runtime", "MCP · State · Recovery", "Give each action clear boundaries"), ("Evaluation", "Traces · Assertions · Replay", "Make improvement measurable")]
    body = ""
    icons = ['<path d="M0 0 H24 V28 H0 Z M6 8 H18 M6 14 H18 M6 20 H14"/>', '<path d="M0 5 H28 M0 15 H28 M0 25 H28"/><circle cx="8" cy="5" r="3" fill="#F3FAFB"/><circle cx="20" cy="15" r="3" fill="#F3FAFB"/><circle cx="10" cy="25" r="3" fill="#F3FAFB"/>', '<path d="M14 0 L27 5 V16 Q26 24 14 30 Q2 24 1 16 V5 Z M7 14 L12 19 L21 10"/>']
    for i, (title, tools, purpose) in enumerate(topics):
        x, y, w, h = (1, 1+i*136, 718, 119) if mobile else (1+i*408, 1, 382, 187)
        color = BLUE if i == 0 else MINT
        body += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{("#F4FAFE", "#F3FAFB", "#F0F9F5")[i]}" stroke="#DDEBEA"/>'
        ix, iy = x+26, y+26
        body += f'<g transform="translate({ix} {iy})" stroke="{color}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">{icons[i]}</g>'
        body += text(x+75, y+48, title, 29, INK, 600)
        body += text(x+75 if mobile else x+26, y+81 if mobile else y+105, tools, 22 if mobile else 20, MUTED)
        body += text(x+75 if mobile else x+26, y+108 if mobile else y+150, purpose, 20 if mobile else 19, MUTED)
        if not mobile:
            body += f'<path d="M{x+26} {y+170} H{x+356}" stroke="#DCEAE9"/><path class="flow-slow" d="M{x+26} {y+170} H{x+356}" stroke="{color}" stroke-width="2"/>'
    return svg(body, 394 if mobile else 189, "关注方向" if zh else "Engineering focus", animated, 720 if mobile else 1200, framed=False)


def focus_mobile(lang, animated):
    return focus(lang, animated, mobile=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for lang in ("zh", "en"):
        for name, renderer in (("hero", hero), ("project", project), ("footer", footer), ("hero-mobile", hero_mobile), ("project-mobile", project_mobile), ("craft", craft), ("craft-mobile", craft_mobile), ("focus", focus), ("focus-mobile", focus_mobile)):
            for animated in (True, False):
                suffix = "" if animated else "-static"
                (OUT / f"{name}-{lang}{suffix}.svg").write_text(renderer(lang, animated), encoding="utf-8", newline="\n")
    print("Generated 36 bilingual desktop/mobile profile assets.")


if __name__ == "__main__":
    main()
