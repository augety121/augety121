#!/usr/bin/env python3
"""Fetch one public profile snapshot and render both locales. No third-party API."""
import argparse
import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from build_profile_assets import OUT, INK, MUTED, BLUE, MINT, svg, text

QUERY = """query Profile($login: String!, $after: String) {
  user(login: $login) {
    followers { totalCount }
    repositories(first:100, after:$after, ownerAffiliations:[OWNER], isFork:false, privacy:PUBLIC) {
      totalCount nodes { stargazerCount }
      pageInfo { hasNextPage endCursor }
    }
    contributionsCollection {
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount weekday } }
      }
    }
  }
}"""


def request_page(token, username, cursor):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": username, "after": cursor}}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json", "User-Agent": "github-profile-builder"},
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        payload = json.load(response)
    if payload.get("errors") or not payload.get("data", {}).get("user"):
        raise RuntimeError("GitHub returned an incomplete profile; keeping the previous assets.")
    return payload["data"]["user"]


def fetch_profile(token, username):
    cursor, stars, seen = None, 0, set()
    profile = None
    while True:
        user = request_page(token, username, cursor)
        repos = user["repositories"]
        if profile is None:
            calendar = user["contributionsCollection"]["contributionCalendar"]
            profile = {"repositories": repos["totalCount"], "followers": user["followers"]["totalCount"], "contributions": calendar["totalContributions"], "weeks": calendar["weeks"]}
        stars += sum(r["stargazerCount"] for r in repos["nodes"])
        page = repos["pageInfo"]
        if not page["hasNextPage"]:
            break
        cursor = page["endCursor"]
        if not cursor or cursor in seen:
            raise RuntimeError("Invalid repository pagination; keeping the previous assets.")
        seen.add(cursor)
    profile.update(stars=stars, updated=datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M UTC+8"))
    return profile


def render_stats(profile, lang, mobile=False):
    zh = lang == "zh"
    body = text(36, 38, "持续积累 / GitHub 足迹" if zh else "SMALL STEPS / GITHUB ACTIVITY", 15, MUTED, 600)
    labels = ["公开原创仓库", "获得星标", "近一年贡献", "关注者"] if zh else ["Public non-fork repos", "Stars received", "Contributions / year", "Followers"]
    for i, (key, label) in enumerate(zip(("repositories", "stars", "contributions", "followers"), labels)):
        x = 36 + (i % 2) * 350 if mobile else 36 + i * 292
        y = (i // 2) * 110 if mobile else 0
        value = profile.get(key)
        body += text(x, 98+y, f"{value:,}" if isinstance(value, int) else "—", 44 if mobile else 40, BLUE if i % 2 == 0 else MINT, 650)
        body += text(x, 129+y, label, 20 if mobile else 17, MUTED)
        if i and not mobile:
            body += f'<path d="M{x-24} 62 V132" stroke="#DAE8E8"/>'
    updated = profile.get("updated")
    caption = ("更新于 " if zh else "Updated ") + updated if updated else ("等待首次 Actions 更新 · 不展示模拟数据" if zh else "Awaiting the first Actions update · No simulated data")
    body += text(36, 283 if mobile else 170, caption, 16 if mobile else 13, MUTED)
    return svg(body, 310 if mobile else 192, "GitHub 动态" if zh else "GitHub activity", False, 720 if mobile else 1200)


def render_calendar(profile):
    body = text(36, 36, "贡献日历 / Contributions", 16, MUTED, 600)
    weeks = profile.get("weeks", [])[-53:]
    if not weeks:
        body += text(600, 115, "等待首次更新 / Awaiting first update", 23, MUTED, 400, 'text-anchor="middle"')
        return svg(body, 200, "贡献日历尚未更新 / Contribution calendar pending", False)
    colors = ["#EAF2F4", "#D4EDE7", "#ABDBCf", "#75C4B3", "#3CA28E"]
    for column, week in enumerate(weeks):
        for day in week["contributionDays"]:
            count = day["contributionCount"]
            level = 0 if count == 0 else 1 if count == 1 else 2 if count < 4 else 3 if count < 7 else 4
            x, y = 44 + column * 21, 56 + day["weekday"] * 18
            from html import escape
            body += f'<rect x="{x}" y="{y}" width="15" height="13" rx="3" fill="{colors[level]}"><title>{escape(day["date"])}: {count}</title></rect>'
    return svg(body, 200, "GitHub 贡献日历 / GitHub contribution calendar", False)


def write_assets(profile, out=OUT, placeholder=False):
    # Fetch/validate everything before overwriting any tracked asset.
    rendered = {f"stats-{lang}.svg": render_stats(profile, lang) for lang in ("zh", "en")}
    rendered.update({f"stats-mobile-{lang}.svg": render_stats(profile, lang, True) for lang in ("zh", "en")})
    rendered["contributions-static.svg"] = render_calendar(profile)
    if placeholder:
        rendered["contribution-snake.svg"] = render_calendar({})
    out.mkdir(parents=True, exist_ok=True)
    for name, content in rendered.items():
        (out / name).write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--placeholder", action="store_true", help="Only for initial setup; never use in the scheduled workflow")
    parser.add_argument("--output-dir", type=Path, default=OUT)
    args = parser.parse_args()
    if args.placeholder:
        profile = {}
    else:
        token, username = os.environ.get("GITHUB_TOKEN"), os.environ.get("GITHUB_USERNAME")
        if not token or not username:
            parser.error("GITHUB_TOKEN and GITHUB_USERNAME are required")
        profile = fetch_profile(token, username)
    write_assets(profile, args.output_dir, args.placeholder)
    print("Updated Chinese/English cards and the reduced-motion contribution calendar.")


if __name__ == "__main__":
    main()
