#!/usr/bin/env python3
"""Generate a repository-local, rate-limit-resistant GitHub profile SVG."""
 
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


GRAPHQL_ENDPOINT = "https://api.github.com/graphql"
QUERY = """
query ProfileDynamics($login: String!) {
  user(login: $login) {
    followers { totalCount }
    repositories(
      first: 100
      ownerAffiliations: [OWNER]
      isFork: false
      privacy: PUBLIC
    ) {
      totalCount
      nodes { stargazerCount }
    }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            date
            contributionCount
            weekday
          }
        }
      }
    }
  }
}
"""


def fetch_profile(token: str, username: str) -> dict:
    payload = json.dumps(
        {"query": QUERY, "variables": {"login": username}}
    ).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "User-Agent": "repository-local-profile-dynamics",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")
        raise RuntimeError(f"GitHub API request failed: HTTP {exc.code}: {detail}") from exc

    if result.get("errors"):
        raise RuntimeError(f"GitHub GraphQL error: {result['errors']}")

    user = result.get("data", {}).get("user")
    if not user:
        raise RuntimeError(f"GitHub user not found: {username}")

    repositories = user["repositories"]
    contributions = user["contributionsCollection"]
    calendar = contributions["contributionCalendar"]

    return {
        "repositories": repositories["totalCount"],
        "stars": sum(repo["stargazerCount"] for repo in repositories["nodes"]),
        "contributions": calendar["totalContributions"],
        "followers": user["followers"]["totalCount"],
        "commits": contributions["totalCommitContributions"],
        "pull_requests": contributions["totalPullRequestContributions"],
        "issues": contributions["totalIssueContributions"],
        "weeks": calendar["weeks"],
        "placeholder": False,
    }


def placeholder_profile() -> dict:
    return {
        "repositories": "—",
        "stars": "—",
        "contributions": "—",
        "followers": "—",
        "commits": 0,
        "pull_requests": 0,
        "issues": 0,
        "weeks": [],
        "placeholder": True,
    }


def contribution_color(count: int) -> str:
    if count <= 0:
        return "#E9EFF4"
    if count == 1:
        return "#DDE9FF"
    if count <= 3:
        return "#C4CBFF"
    if count <= 6:
        return "#8C93F4"
    return "#67BDB3"


def format_value(value: object) -> str:
    return f"{value:,}" if isinstance(value, int) else str(value)


def render_svg(profile: dict) -> str:
    width = 920
    height = 338
    cell = 10
    gap = 3
    grid_x = 115
    grid_y = 206
    stat_labels = ("公开仓库", "累计星标", "年度贡献", "关注者")
    stat_keys = ("repositories", "stars", "contributions", "followers")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub 动态">',
        "<defs>",
        '<linearGradient id="surface" x1="0" y1="0" x2="1" y2="1">',
        '<stop offset="0%" stop-color="#FEFDF9"/>',
        '<stop offset="48%" stop-color="#F8F8FF"/>',
        '<stop offset="100%" stop-color="#F3FBF9"/>',
        "</linearGradient>",
        '<linearGradient id="flow" x1="0" y1="0" x2="1" y2="0">',
        '<stop offset="0%" stop-color="#A8DDF0"/>',
        '<stop offset="48%" stop-color="#9EA6F8"/>',
        '<stop offset="100%" stop-color="#92D5C9"/>',
        "</linearGradient>",
        '<radialGradient id="orb-blue" cx="32%" cy="24%" r="78%">',
        '<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.98"/>',
        '<stop offset="60%" stop-color="#EAF4FF" stop-opacity="0.88"/>',
        '<stop offset="100%" stop-color="#D9E8FA" stop-opacity="0.72"/>',
        "</radialGradient>",
        '<radialGradient id="orb-mint" cx="32%" cy="24%" r="78%">',
        '<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.98"/>',
        '<stop offset="60%" stop-color="#EAF9F5" stop-opacity="0.88"/>',
        '<stop offset="100%" stop-color="#D9F0EB" stop-opacity="0.72"/>',
        "</radialGradient>",
        '<radialGradient id="orb-violet" cx="32%" cy="24%" r="78%">',
        '<stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.98"/>',
        '<stop offset="60%" stop-color="#F0EFFF" stop-opacity="0.9"/>',
        '<stop offset="100%" stop-color="#E2E1FA" stop-opacity="0.74"/>',
        "</radialGradient>",
        '<filter id="soft-shadow" x="-35%" y="-35%" width="170%" height="180%">',
        '<feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#7283A8" flood-opacity="0.13"/>',
        "</filter>",
        '<filter id="blur" x="-50%" y="-50%" width="200%" height="200%">',
        '<feGaussianBlur stdDeviation="18"/>',
        "</filter>",
        "<style>",
        "text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI','Microsoft YaHei',Arial,sans-serif}",
        ".eyebrow{font-size:12px;font-weight:600;letter-spacing:2px;fill:#77839A}",
        ".subtitle{font-size:11px;fill:#9AA4B5}",
        ".value{font-size:22px;font-weight:700;fill:#3D4864}",
        ".label{font-size:11px;font-weight:500;fill:#7A869C}",
        ".panel-title{font-size:12px;font-weight:600;fill:#6E7A91}",
        ".micro{font-size:10px;fill:#98A2B3}",
        "</style>",
        "</defs>",
        '<rect x="1" y="1" width="918" height="336" rx="24" fill="url(#surface)" stroke="#E7EAF0"/>',
        '<ellipse cx="112" cy="54" rx="95" ry="46" fill="#DDF2FF" opacity="0.42" filter="url(#blur)"/>',
        '<ellipse cx="778" cy="78" rx="108" ry="48" fill="#E7E4FF" opacity="0.46" filter="url(#blur)"/>',
        '<ellipse cx="704" cy="280" rx="120" ry="42" fill="#DCF5EE" opacity="0.38" filter="url(#blur)"/>',
        '<text x="34" y="32" class="eyebrow">公开活动概览</text>',
        '<text x="886" y="32" class="subtitle" text-anchor="end">由仓库工作流每日更新</text>',
        '<path d="M96 103 C166 50 229 147 306 98 S442 50 516 101 S655 149 724 97 S825 65 866 103" fill="none" stroke="url(#flow)" stroke-width="2" opacity="0.55"/>',
        '<path d="M100 114 C180 151 239 64 319 110 S461 151 538 108 S676 65 754 111 S839 132 870 107" fill="none" stroke="#FFFFFF" stroke-width="5" opacity="0.52"/>',
    ]

    orb_gradients = ("orb-blue", "orb-mint", "orb-violet", "orb-blue")
    orb_strokes = ("#CFE5F6", "#CDEAE3", "#D9D7F5", "#D5E6F4")
    orb_centers = (145, 355, 565, 775)
    for index, (label, key) in enumerate(zip(stat_labels, stat_keys)):
        x = orb_centers[index]
        parts.extend(
            [
                f'<circle cx="{x}" cy="104" r="45" fill="url(#{orb_gradients[index]})" stroke="{orb_strokes[index]}" stroke-width="1.2" filter="url(#soft-shadow)"/>',
                f'<circle cx="{x - 13}" cy="88" r="12" fill="#FFFFFF" opacity="0.3"/>',
                f'<text x="{x}" y="105" class="value" text-anchor="middle">{format_value(profile[key])}</text>',
                f'<text x="{x}" y="126" class="label" text-anchor="middle">{label}</text>',
            ]
        )

    parts.extend(
        [
            '<rect x="34" y="166" width="852" height="132" rx="18" fill="#FFFFFF" fill-opacity="0.58" stroke="#FFFFFF" stroke-opacity="0.92" filter="url(#soft-shadow)"/>',
            '<rect x="35" y="167" width="850" height="130" rx="17" fill="none" stroke="#DEE7F0" stroke-opacity="0.72"/>',
            '<text x="58" y="191" class="panel-title">过去 12 个月的贡献记录</text>',
            '<text x="94" y="222" class="micro" text-anchor="middle">一</text>',
            '<text x="94" y="248" class="micro" text-anchor="middle">三</text>',
            '<text x="94" y="274" class="micro" text-anchor="middle">五</text>',
        ]
    )

    weeks = profile["weeks"][-53:]
    offset = 53 - len(weeks)
    day_lookup: dict[tuple[int, int], dict] = {}
    for week_index, week in enumerate(weeks):
        for day in week.get("contributionDays", []):
            row = int(day.get("weekday", 0)) % 7
            day_lookup[(week_index + offset, row)] = day

    for week_index in range(53):
        for row in range(7):
            day = day_lookup.get((week_index, row), {})
            count = int(day.get("contributionCount", 0))
            date = day.get("date", "暂无数据")
            x = grid_x + week_index * (cell + gap)
            y = grid_y + row * (cell + gap)
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{contribution_color(count)}"><title>{date}：{count} 次贡献</title></rect>'
            )

    legend_x = 750
    parts.append(f'<text x="{legend_x - 23}" y="191" class="micro">少</text>')
    for index, color in enumerate(("#E9EFF4", "#DDE9FF", "#C4CBFF", "#8C93F4", "#67BDB3")):
        parts.append(f'<rect x="{legend_x + index * 14}" y="181" width="9" height="9" rx="3" fill="{color}"/>')
    parts.append(f'<text x="{legend_x + 74}" y="191" class="micro">多</text>')

    if profile["placeholder"]:
        footer = "首次运行工作流后自动更新"
    else:
        updated = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M")
        footer = (
            f"提交 {profile['commits']} · Pull Request {profile['pull_requests']} · "
            f"Issue {profile['issues']} · 更新于 {updated}"
        )
    parts.append('<circle cx="35" cy="318" r="3" fill="#8C93F4" opacity="0.72"/>')
    parts.append(f'<text x="46" y="322" class="micro">{footer}</text>')
    parts.append("</svg>")
    return "".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="github-dynamics.svg")
    parser.add_argument("--placeholder", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.placeholder:
        profile = placeholder_profile()
    else:
        token = os.environ.get("GITHUB_TOKEN", "")
        username = os.environ.get("GITHUB_USERNAME", "")
        if not token or not username:
            print("GITHUB_TOKEN and GITHUB_USERNAME are required", file=sys.stderr)
            return 2
        profile = fetch_profile(token, username)

    output = Path(args.output)
    output.write_text(render_svg(profile), encoding="utf-8")
    print(f"Generated {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
