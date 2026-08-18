#!/usr/bin/env python3
"""Generate the light visual system used by the augety121 profile README.

The assets intentionally use only GitHub-safe SVG primitives and system font
fallbacks. No remote fonts, scripts, or CSS resources are required at render time.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

BG = "#F7FBFF"
SURFACE = "#FFFFFF"
SURFACE_ALT = "#F3F8FF"
TEXT = "#10233F"
MUTED = "#61738D"
MUTED2 = "#8AA0BB"
BORDER = "#DCE8F6"
BLUE = "#4F7CFF"
CYAN = "#4CB9E9"
MINT = "#48C9B0"
VIOLET = "#8D7CF7"
ICE = "#EAF3FF"
BLUE_SOFT = "#DCE9FF"
CYAN_SOFT = "#DCF6FF"
MINT_SOFT = "#DDF8F1"
VIOLET_SOFT = "#EEE9FF"

FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Microsoft YaHei','PingFang SC','Noto Sans CJK SC',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"


def defs(extra: str = "") -> str:
    return f"""
<defs>
  <linearGradient id="page" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#FBFDFF"/>
    <stop offset="0.55" stop-color="#F6FAFF"/>
    <stop offset="1" stop-color="#F0F7FF"/>
  </linearGradient>
  <linearGradient id="brand" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{BLUE}"/>
    <stop offset="0.53" stop-color="{CYAN}"/>
    <stop offset="1" stop-color="{MINT}"/>
  </linearGradient>
  <linearGradient id="brandSoft" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#E9F0FF"/>
    <stop offset="0.55" stop-color="#EAFBFF"/>
    <stop offset="1" stop-color="#ECFBF6"/>
  </linearGradient>
  <radialGradient id="blobBlue"><stop offset="0" stop-color="#BED4FF" stop-opacity=".6"/><stop offset="1" stop-color="#BED4FF" stop-opacity="0"/></radialGradient>
  <radialGradient id="blobCyan"><stop offset="0" stop-color="#C5F0FF" stop-opacity=".55"/><stop offset="1" stop-color="#C5F0FF" stop-opacity="0"/></radialGradient>
  <radialGradient id="blobMint"><stop offset="0" stop-color="#CCF5E9" stop-opacity=".5"/><stop offset="1" stop-color="#CCF5E9" stop-opacity="0"/></radialGradient>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="160%">
    <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="#466887" flood-opacity=".10"/>
  </filter>
  <filter id="shadowSmall" x="-20%" y="-20%" width="140%" height="150%">
    <feDropShadow dx="0" dy="6" stdDeviation="10" flood-color="#466887" flood-opacity=".08"/>
  </filter>
  <filter id="blur"><feGaussianBlur stdDeviation="28"/></filter>
  <style>
    text{{font-family:{FONT}}}
    .mono{{font-family:{MONO}}}
    .eyebrow{{font-family:{MONO};font-size:13px;font-weight:700;letter-spacing:2.2px;fill:{MUTED2}}}
    .title{{font-size:48px;font-weight:800;letter-spacing:-2px;fill:{TEXT}}}
    .title-en{{font-size:50px;font-weight:800;letter-spacing:-1.7px;fill:{TEXT}}}
    .body{{font-size:18px;fill:{MUTED}}}
    .body-sm{{font-size:14px;fill:{MUTED}}}
    .label{{font-size:12px;font-weight:700;fill:{MUTED}}}
    .card-title{{font-size:17px;font-weight:760;fill:{TEXT}}}
    .card-sub{{font-size:12px;fill:{MUTED}}}
    .micro{{font-family:{MONO};font-size:10px;letter-spacing:1.1px;fill:{MUTED2}}}
    .tag{{font-size:12px;font-weight:700;fill:{TEXT}}}
  </style>
  {extra}
</defs>"""


def card(x: int, y: int, w: int, h: int, rx: int = 20, fill: str = SURFACE, shadow: bool = False) -> str:
    flt = ' filter="url(#shadowSmall)"' if shadow else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{BORDER}"{flt}/>'


def write(name: str, svg: str) -> None:
    (ASSETS / name).write_text(svg.strip() + "\n", encoding="utf-8")


def hero(lang: str) -> str:
    zh = lang == "zh"
    title = "Reliable Agent Systems"
    subtitle = "Built to be verifiable — not just impressive in a demo."
    headline_class = "title-en"
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="440" viewBox="0 0 1200 440" role="img" aria-label="augety121 — {title}">
{defs()}
<rect x="1" y="1" width="1198" height="438" rx="34" fill="url(#page)" stroke="{BORDER}"/>
<circle cx="105" cy="42" r="190" fill="url(#blobBlue)" filter="url(#blur)"/>
<circle cx="1098" cy="84" r="210" fill="url(#blobCyan)" filter="url(#blur)"/>
<circle cx="1014" cy="390" r="170" fill="url(#blobMint)" filter="url(#blur)"/>

<!-- slim visual identity rail -->
<rect x="42" y="46" width="7" height="348" rx="4" fill="url(#brand)"/>

<g transform="translate(76 58)">
  <rect x="0" y="0" width="162" height="30" rx="15" fill="{SURFACE}" stroke="{BORDER}"/>
  <circle cx="18" cy="15" r="5" fill="{MINT}">
    <animate attributeName="opacity" values="1;.35;1" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <text x="32" y="20" class="micro" style="font-weight:700">OPEN SOURCE / ACTIVE</text>
</g>

<text x="76" y="132" class="eyebrow">AUGETY121 · AGENT SYSTEMS</text>
<text x="76" y="201" class="title">{title}</text>
<text x="76" y="241" class="body">{subtitle}</text>
<text x="76" y="278" class="body">RAG · Context Engineering · MCP · Runtime · Evaluation</text>

<!-- compact capability chips -->
<g transform="translate(76 319)">
  <g>{card(0,0,126,48,16,SURFACE,True)}<circle cx="20" cy="24" r="5" fill="{BLUE}"/><text x="36" y="29" class="tag">Evidence</text></g>
  <g transform="translate(138 0)">{card(0,0,126,48,16,SURFACE,True)}<circle cx="20" cy="24" r="5" fill="{CYAN}"/><text x="36" y="29" class="tag">Context</text></g>
  <g transform="translate(276 0)">{card(0,0,110,48,16,SURFACE,True)}<circle cx="20" cy="24" r="5" fill="{VIOLET}"/><text x="36" y="29" class="tag">Tools</text></g>
  <g transform="translate(398 0)">{card(0,0,108,48,16,SURFACE,True)}<circle cx="20" cy="24" r="5" fill="{MINT}"/><text x="36" y="29" class="tag">State</text></g>
</g>

<!-- runtime canvas -->
<g transform="translate(666 48)">
  <rect x="0" y="0" width="488" height="344" rx="30" fill="#FFFFFF" fill-opacity=".84" stroke="{BORDER}" filter="url(#shadow)"/>
  <text x="28" y="34" class="micro">RELIABLE AGENT LOOP</text>

  <path id="orbit" d="M113 83 C223 37 340 46 392 133 C440 212 369 285 250 294 C130 303 51 247 57 167 C60 125 79 102 113 83Z" fill="none" stroke="#C5D8F4" stroke-width="2" stroke-dasharray="6 8"/>
  <circle r="5" fill="{BLUE}"><animateMotion dur="8s" repeatCount="indefinite"><mpath href="#orbit"/></animateMotion></circle>

  <!-- flow nodes -->
  <g transform="translate(30 68)">{card(0,0,128,62,17,SURFACE_ALT)}<circle cx="20" cy="20" r="5" fill="{BLUE}"/><text x="20" y="44" class="card-title">Retrieve</text><text x="20" y="57" class="card-sub">evidence first</text></g>
  <g transform="translate(330 68)">{card(0,0,128,62,17,SURFACE_ALT)}<circle cx="20" cy="20" r="5" fill="{CYAN}"/><text x="20" y="44" class="card-title">Context</text><text x="20" y="57" class="card-sub">budget + memory</text></g>
  <g transform="translate(330 226)">{card(0,0,128,62,17,SURFACE_ALT)}<circle cx="20" cy="20" r="5" fill="{MINT}"/><text x="20" y="44" class="card-title">Evaluate</text><text x="20" y="57" class="card-sub">trace + state</text></g>
  <g transform="translate(30 226)">{card(0,0,128,62,17,SURFACE_ALT)}<circle cx="20" cy="20" r="5" fill="{VIOLET}"/><text x="20" y="44" class="card-title">Tools</text><text x="20" y="57" class="card-sub">bounded actions</text></g>

  <g transform="translate(164 121)">
    <rect x="0" y="0" width="160" height="118" rx="28" fill="url(#brand)"/>
    <text x="80" y="45" text-anchor="middle" style="font-family:{FONT};font-size:18px;font-weight:800;fill:#fff">Agent Runtime</text>
    <text x="80" y="69" text-anchor="middle" style="font-family:{FONT};font-size:11px;fill:#fff;opacity:.86">reason · state · recover</text>
    <rect x="46" y="88" width="68" height="5" rx="3" fill="#fff" opacity=".25"/>
    <rect x="46" y="88" width="26" height="5" rx="3" fill="#fff" opacity=".9">
      <animate attributeName="width" values="26;68;26" dur="3.2s" repeatCount="indefinite"/>
    </rect>
  </g>
</g>

<text x="76" y="404" class="micro">EVIDENCE · CONTEXT · ACTION · STATE · EVALUATION</text>
</svg>
"""


def project_card() -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="350" viewBox="0 0 1200 350" role="img" aria-label="MCP State Twin — deterministic forkable stateful MCP test worlds">
{defs()}
<rect x="1" y="1" width="1198" height="348" rx="30" fill="url(#page)" stroke="{BORDER}"/>
<circle cx="1060" cy="32" r="180" fill="url(#blobCyan)" filter="url(#blur)"/>
<rect x="36" y="34" width="78" height="26" rx="13" fill="{BLUE_SOFT}"/><text x="75" y="51" text-anchor="middle" class="micro" style="fill:{BLUE};font-weight:800">FEATURED</text>
<text x="36" y="104" style="font-family:{FONT};font-size:36px;font-weight:820;fill:{TEXT};letter-spacing:-1px">MCP State Twin</text>
<text x="36" y="137" class="body">Deterministic · Forkable · Stateful · Reproducible</text>
<text x="36" y="181" class="body-sm">Stateful MCP test worlds for reproducible AI agent evaluation.</text>
<text x="36" y="205" class="body-sm">Fork one immutable snapshot, execute isolated trajectories, compare terminal worlds.</text>

<g transform="translate(36 236)">
  <g>{card(0,0,120,42,14,SURFACE)}<text x="60" y="26" text-anchor="middle" class="tag">Go</text></g>
  <g transform="translate(130 0)">{card(0,0,140,42,14,SURFACE)}<text x="70" y="26" text-anchor="middle" class="tag">MCP</text></g>
  <g transform="translate(280 0)">{card(0,0,180,42,14,SURFACE)}<text x="90" y="26" text-anchor="middle" class="tag">Agent Evaluation</text></g>
  <g transform="translate(470 0)">{card(0,0,140,42,14,SURFACE)}<text x="70" y="26" text-anchor="middle" class="tag">SQLite</text></g>
</g>

<!-- fork visualization -->
<g transform="translate(660 42)">
  <text x="0" y="20" class="micro">SNAPSHOT · FORK · ACT · ASSERT · DIFF</text>
  <g transform="translate(8 58)">
    <rect x="0" y="0" width="150" height="56" rx="18" fill="{SURFACE}" stroke="{BORDER}" filter="url(#shadowSmall)"/>
    <circle cx="24" cy="28" r="7" fill="{BLUE}"/>
    <text x="45" y="25" class="card-title">Snapshot S₀</text><text x="45" y="43" class="card-sub">immutable start</text>
  </g>
  <path d="M158 86 C198 86 198 50 230 50" fill="none" stroke="{BLUE}" stroke-width="2.2"/>
  <path d="M158 86 C198 86 198 122 230 122" fill="none" stroke="{CYAN}" stroke-width="2.2"/>
  <path d="M158 86 C198 86 198 194 230 194" fill="none" stroke="{MINT}" stroke-width="2.2"/>
  <g transform="translate(230 21)">{card(0,0,140,58,18,SURFACE)}<circle cx="22" cy="29" r="6" fill="{BLUE}"/><text x="42" y="26" class="card-title">Fork A</text><text x="42" y="44" class="card-sub">trajectory α</text></g>
  <g transform="translate(230 93)">{card(0,0,140,58,18,SURFACE)}<circle cx="22" cy="29" r="6" fill="{CYAN}"/><text x="42" y="26" class="card-title">Fork B</text><text x="42" y="44" class="card-sub">trajectory β</text></g>
  <g transform="translate(230 165)">{card(0,0,140,58,18,SURFACE)}<circle cx="22" cy="29" r="6" fill="{MINT}"/><text x="42" y="26" class="card-title">Fork C</text><text x="42" y="44" class="card-sub">trajectory γ</text></g>
  <path d="M370 50 C386 50 390 90 395 118" fill="none" stroke="#B7C9DE" stroke-width="2"/>
  <path d="M370 122 L395 122" fill="none" stroke="#B7C9DE" stroke-width="2"/>
  <path d="M370 194 C386 194 390 154 395 126" fill="none" stroke="#B7C9DE" stroke-width="2"/>
  <g transform="translate(395 88)">
    <rect x="0" y="0" width="120" height="70" rx="20" fill="url(#brand)"/>
    <text x="60" y="30" text-anchor="middle" style="font-family:{FONT};font-size:15px;font-weight:800;fill:#fff">Terminal</text>
    <text x="60" y="51" text-anchor="middle" style="font-family:{FONT};font-size:11px;fill:#fff;opacity:.9">canonical diff</text>
  </g>
</g>
<text x="36" y="323" class="micro">PRODUCTION WRITES: NONE · MODEL TRAJECTORIES MAY DIFFER · TERMINAL STATE IS COMPARABLE</text>
</svg>
"""


def focus_map() -> str:
    items = [
        ("Retrieval", "evidence · hybrid · rerank", BLUE, BLUE_SOFT),
        ("Context Engineering", "memory · budget · selection", CYAN, CYAN_SOFT),
        ("Agent Runtime", "state · recover · checkpoint", VIOLET, VIOLET_SOFT),
        ("MCP &amp; Tooling", "contracts · isolation · permissions", BLUE, ICE),
        ("Evaluation", "trace · assertions · terminal state", MINT, MINT_SOFT),
        ("Safety", "boundaries · least privilege · audit", CYAN, CYAN_SOFT),
    ]
    chunks = []
    positions = [(28, 58), (405, 58), (782, 58), (28, 176), (405, 176), (782, 176)]
    for (title, sub, color, fill), (x, y) in zip(items, positions):
        chunks.append(
            f'{card(x,y,350,90,22,SURFACE,True)}'
            f'<rect x="{x+18}" y="{y+18}" width="42" height="42" rx="13" fill="{fill}"/>'
            f'<circle cx="{x+39}" cy="{y+39}" r="7" fill="{color}"/>'
            f'<text x="{x+78}" y="{y+38}" class="card-title">{title}</text>'
            f'<text x="{x+78}" y="{y+61}" class="card-sub">{sub}</text>'
        )
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Engineering focus map">
{defs()}
<rect x="1" y="1" width="1198" height="298" rx="30" fill="{BG}" stroke="{BORDER}"/>
<text x="28" y="34" class="micro">ENGINEERING RADAR / RELIABLE AGENT SYSTEMS</text>
{''.join(chunks)}
</svg>
"""


def system_map() -> str:
    stages = [
        ("Knowledge", "source", BLUE, BLUE_SOFT),
        ("Retrieve", "search", BLUE, ICE),
        ("Evidence", "rerank", CYAN, CYAN_SOFT),
        ("Context", "select", VIOLET, VIOLET_SOFT),
        ("Runtime", "reason", BLUE, BLUE_SOFT),
        ("Tools", "act", MINT, MINT_SOFT),
        ("Evaluate", "verify", CYAN, CYAN_SOFT),
    ]
    x0, gap, w, y = 30, 12, 146, 92
    chunks = []
    for i, (title, sub, color, fill) in enumerate(stages):
        x = x0 + i * (w + gap)
        chunks.append(
            f'{card(x,y,w,92,22,SURFACE,True)}'
            f'<rect x="{x+16}" y="{y+16}" width="34" height="34" rx="11" fill="{fill}"/>'
            f'<circle cx="{x+33}" cy="{y+33}" r="6" fill="{color}"/>'
            f'<text x="{x+16}" y="{y+72}" class="card-title">{title}</text>'
            f'<text x="{x+w-16}" y="{y+30}" class="micro" text-anchor="end">{sub.upper()}</text>'
        )
        if i < len(stages)-1:
            ax = x + w + 2
            chunks.append(f'<path d="M{ax} {y+46} H{ax+8}" stroke="#AFC4DA" stroke-width="2.2" stroke-linecap="round"/><path d="M{ax+5} {y+42} L{ax+10} {y+46} L{ax+5} {y+50}" fill="none" stroke="#AFC4DA" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>')
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250" role="img" aria-label="From knowledge to reliable action and evaluation">
{defs()}
<rect x="1" y="1" width="1198" height="248" rx="30" fill="url(#page)" stroke="{BORDER}"/>
<text x="30" y="38" class="micro">SYSTEM VIEW / FROM KNOWLEDGE TO VERIFIABLE ACTION</text>
<text x="30" y="65" class="body-sm">Reliable agents connect evidence, context, tools, state and evaluation into one inspectable system.</text>
{''.join(chunks)}
<text x="30" y="222" class="micro">WHY THIS CONTEXT? · WHAT CHANGED? · HOW DO WE VERIFY IT?</text>
</svg>
"""


def footer() -> str:
    return f"""
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="180" viewBox="0 0 1200 180" role="img" aria-label="augety121 footer">
{defs()}
<rect x="1" y="1" width="1198" height="178" rx="28" fill="url(#page)" stroke="{BORDER}"/>
<path d="M1 112 C160 64 300 154 460 104 C650 44 760 160 936 111 C1040 82 1110 88 1199 116 L1199 179 L1 179Z" fill="url(#brandSoft)"/>
<path d="M0 116 C168 69 308 155 470 108 C646 58 790 151 946 116 C1047 93 1122 96 1200 120" fill="none" stroke="url(#brand)" stroke-width="2" opacity=".55"/>
<text x="600" y="58" text-anchor="middle" style="font-family:{FONT};font-size:20px;font-weight:760;fill:{TEXT}">Evidence · Context · Action · State · Evaluation</text>
<text x="600" y="87" text-anchor="middle" class="body-sm">Retrieval with evidence. Context with intent. Actions with boundaries. Evaluation with state.</text>
<text x="600" y="149" text-anchor="middle" class="micro">AUGETY121 · AGENT SYSTEMS · OPEN SOURCE</text>
</svg>
"""


write("hero-zh-light.svg", hero("zh"))
write("hero-en-light.svg", hero("en"))
write("mcp-state-twin-light.svg", project_card())
write("focus-map-light.svg", focus_map())
write("system-map-light.svg", system_map())
write("footer-light.svg", footer())
print("Generated profile visual assets")
