#!/usr/bin/env python3
"""Generate repository-local GitHub profile dynamics cards (light/dark)."""

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
    repositories(first: 100, ownerAffiliations: [OWNER], isFork: false, privacy: PUBLIC) {
      totalCount
      nodes { stargazerCount }
    }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
  }
}
"""

PALETTES = {
    "light": {
        "bg": "#F7FBFF",
        "panel": "#FFFFFF",
        "panel2": "#F3F8FF",
        "stroke": "#DCE8F6",
        "text": "#10233F",
        "muted": "#61738D",
        "muted2": "#8AA0BB",
        "indigo": "#4F7CFF",
        "cyan": "#4CB9E9",
        "mint": "#48C9B0",
        "heat": ["#EEF4FB", "#DCE9FF", "#BDD3FF", "#7DA5FF", "#48C9B0"],
    },
    "dark": {
        "bg": "#070B14",
        "panel": "#0F172A",
        "panel2": "#111B30",
        "stroke": "#24324A",
        "text": "#EAF1FF",
        "muted": "#9FB0C8",
        "muted2": "#70829B",
        "indigo": "#8B85FF",
        "cyan": "#5BD5FF",
        "mint": "#4BE0C4",
        "heat": ["#18243A", "#253C64", "#405FA8", "#676FFF", "#36CDB5"],
    },
}


def fetch_profile(token: str, username: str) -> dict:
    payload = json.dumps({"query": QUERY, "variables": {"login": username}}).encode("utf-8")
    request = urllib.request.Request(
        GRAPHQL_ENDPOINT,
        data=payload,
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github+json",
            "User-Agent": "augety121-profile-dynamics",
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

    repos = user["repositories"]
    contributions = user["contributionsCollection"]
    calendar = contributions["contributionCalendar"]
    return {
        "repositories": repos["totalCount"],
        "stars": sum(repo["stargazerCount"] for repo in repos["nodes"]),
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


def fmt(value: object) -> str:
    return f"{value:,}" if isinstance(value, int) else str(value)


def heat_color(count: int, colors: list[str]) -> str:
    if count <= 0:
        return colors[0]
    if count == 1:
        return colors[1]
    if count <= 3:
        return colors[2]
    if count <= 6:
        return colors[3]
    return colors[4]


def render_svg(profile: dict, theme: str) -> str:
    p = PALETTES[theme]
    width, height = 1200, 356
    labels = ("PUBLIC REPOS", "STARS", "CONTRIBUTIONS", "FOLLOWERS")
    keys = ("repositories", "stars", "contributions", "followers")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub 公开活动概览">',
        "<defs>",
        f'<linearGradient id="brand" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{p["indigo"]}"/><stop offset=".52" stop-color="{p["cyan"]}"/><stop offset="1" stop-color="{p["mint"]}"/></linearGradient>',
        f'<style>text{{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Microsoft YaHei","PingFang SC",Arial,sans-serif}}.eyebrow{{font:600 11px ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:2px;fill:{p["muted2"]}}}.value{{font-size:24px;font-weight:760;fill:{p["text"]}}}.label{{font-size:11px;font-weight:600;fill:{p["muted"]}}}.small{{font-size:10px;fill:{p["muted2"]}}}.panel{{font-size:12px;font-weight:700;fill:{p["text"]}}}</style>',
        "</defs>",
        f'<rect x="1" y="1" width="1198" height="354" rx="28" fill="{p["bg"]}" stroke="{p["stroke"]}"/>',
        f'<rect x="0" y="0" width="10" height="356" rx="5" fill="url(#brand)"/>',
        '<text x="42" y="34" class="eyebrow">GITHUB DYNAMICS / PUBLIC ACTIVITY</text>',
    ]

    start_x = 42
    card_w = 252
    gap = 18
    for idx, (label, key) in enumerate(zip(labels, keys)):
        x = start_x + idx * (card_w + gap)
        parts += [
            f'<rect x="{x}" y="52" width="{card_w}" height="78" rx="18" fill="{p["panel"]}" stroke="{p["stroke"]}"/>',
            f'<circle cx="{x+24}" cy="75" r="5" fill="{(p["indigo"], p["cyan"], p["mint"], p["indigo"])[idx]}"/>',
            f'<text x="{x+22}" y="105" class="value">{fmt(profile[key])}</text>',
            f'<text x="{x+card_w-18}" y="104" class="label" text-anchor="end">{label}</text>',
        ]

    parts += [
        f'<rect x="42" y="150" width="1116" height="154" rx="20" fill="{p["panel"]}" stroke="{p["stroke"]}"/>',
        '<text x="68" y="178" class="panel">Last 12 months</text>',
    ]

    cell, gap_cell = 12, 4
    grid_x, grid_y = 118, 198
    weeks = profile["weeks"][-53:]
    offset = 53 - len(weeks)
    lookup: dict[tuple[int, int], dict] = {}
    for week_index, week in enumerate(weeks):
        for day in week.get("contributionDays", []):
            lookup[(week_index + offset, int(day.get("weekday", 0)) % 7)] = day

    for week_index in range(53):
        for row in range(7):
            day = lookup.get((week_index, row), {})
            count = int(day.get("contributionCount", 0))
            date = day.get("date", "暂无数据")
            x = grid_x + week_index * (cell + gap_cell)
            y = grid_y + row * (cell + gap_cell)
            color = heat_color(count, p["heat"])
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="3" fill="{color}"><title>{date}: {count} contributions</title></rect>')

    for label, row in (("M", 1), ("W", 3), ("F", 5)):
        y = grid_y + row * (cell + gap_cell) + 10
        parts.append(f'<text x="94" y="{y}" class="small" text-anchor="middle">{label}</text>')

    legend_x = 965
    parts.append(f'<text x="{legend_x-28}" y="178" class="small">LESS</text>')
    for i, color in enumerate(p["heat"]):
        parts.append(f'<rect x="{legend_x+i*17}" y="168" width="11" height="11" rx="3" fill="{color}"/>')
    parts.append(f'<text x="{legend_x+92}" y="178" class="small">MORE</text>')

    if profile["placeholder"]:
        footer = "Real public activity will be populated after the first workflow run"
    else:
        updated = datetime.now(ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d %H:%M")
        footer = f"Daily update · commits {profile['commits']} · PRs {profile['pull_requests']} · issues {profile['issues']} · Asia/Shanghai {updated}"
    parts += [
        f'<circle cx="48" cy="328" r="4" fill="{p["mint"]}"/>',
        f'<text x="62" y="332" class="small">{footer}</text>',
        "</svg>",
    ]
    return "".join(parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="github-dynamics-light.svg")
    parser.add_argument("--theme", choices=("light", "dark"), default="light")
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

    Path(args.output).write_text(render_svg(profile, args.theme), encoding="utf-8")
    print(f"Generated {args.output} ({args.theme})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
