#!/usr/bin/env python3
"""Build an evidence report for the daily repository-maintenance PR."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REPORT = ROOT / "reports" / "latest.md"
API = "https://api.github.com"
QUERIES = (
    "Chinese webnovel skill",
    "AI writing skill novel",
    "中文 小说 写作 skill",
    "agent skill writing humanizer",
)
RELEVANCE_TERMS = ("writing", "writer", "novel", "story", "prose", "humaniz", "slop", "写作", "小说", "网文", "故事", "文本")


def github_links(text: str) -> list[tuple[str, str]]:
    """Return unique GitHub repository links from Markdown text."""
    found: list[tuple[str, str]] = []
    seen: set[str] = set()
    for label, url in re.findall(r"\[([^\]]+)\]\((https://github\.com/[^)]+)\)", text):
        match = re.match(r"https://github\.com/([^/]+)/([^/#?]+)$", url.rstrip("/"))
        if not match:
            continue
        repo = f"{match.group(1)}/{match.group(2)}"
        if repo.lower() not in seen:
            seen.add(repo.lower())
            found.append((label, repo))
    return found


def request_json(url: str, token: str | None = None) -> dict:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-ai-writing-maintainer"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def repo_status(repo: str, token: str | None) -> dict:
    try:
        data = request_json(f"{API}/repos/{repo}", token)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        return {"repo": repo, "state": "unverified", "error": str(exc)}
    license_data = data.get("license") or {}
    return {
        "repo": repo,
        "state": "ok",
        "archived": data.get("archived", False),
        "fork": data.get("fork", False),
        "stars": data.get("stargazers_count", 0),
        "forks": data.get("forks_count", 0),
        "license": license_data.get("spdx_id") or "UNDECLARED",
        "default_branch": data.get("default_branch", ""),
        "pushed_at": data.get("pushed_at") or "unknown",
        "html_url": data.get("html_url", f"https://github.com/{repo}"),
    }


def discover(query: str, token: str | None) -> list[dict]:
    params = urllib.parse.urlencode({"q": query, "sort": "updated", "order": "desc", "per_page": 10})
    try:
        data = request_json(f"{API}/search/repositories?{params}", token)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
        return [{"query": query, "state": "unverified", "error": str(exc)}]
    results = []
    for item in data.get("items", []):
        if item.get("fork") or item.get("archived"):
            continue
        results.append({
            "query": query,
            "repo": item.get("full_name"),
            "description": item.get("description") or "",
            "stars": item.get("stargazers_count", 0),
            "license": (item.get("license") or {}).get("spdx_id") or "UNDECLARED",
            "pushed_at": item.get("pushed_at") or "unknown",
            "html_url": item.get("html_url"),
        })
    return results


def candidate_score(item: dict, now: datetime) -> tuple[int, list[str]]:
    text = f"{item.get('repo', '')} {item.get('description', '')}".lower()
    if not any(term in text for term in RELEVANCE_TERMS):
        return 0, ["not relevant"]
    score = 3
    reasons = ["topic match"]
    if item.get("license") != "UNDECLARED":
        score += 2
        reasons.append("license declared")
    stars = item.get("stars", 0)
    if stars >= 100:
        score += 2
        reasons.append("100+ stars")
    elif stars >= 10:
        score += 1
        reasons.append("10+ stars")
    try:
        pushed = datetime.fromisoformat(item["pushed_at"].replace("Z", "+00:00"))
        if (now - pushed).days <= 180:
            score += 2
            reasons.append("active within 180 days")
    except (KeyError, ValueError):
        pass
    if item.get("description"):
        score += 1
        reasons.append("description present")
    return score, reasons


def render(inventory: list[dict], candidates: list[dict], now: datetime) -> str:
    lines = [
        "# Daily Update Report",
        "",
        f"> Generated: {now.isoformat(timespec='seconds')} (UTC)",
        "> This report is evidence for review. It does not directly edit `README.md`.",
        "",
        "## Existing Entries",
        "",
        "| Repository | State | License | Stars | Last push | Notes |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for item in inventory:
        if item["state"] != "ok":
            lines.append(f"| `{item['repo']}` | {item['state']} | - | - | - | `{item.get('error', '')}` |")
            continue
        notes = []
        if item["archived"]:
            notes.append("archived")
        if item["license"] == "UNDECLARED":
            notes.append("license undeclared")
        lines.append(
            f"| [{item['repo']}]({item['html_url']}) | ok | {item['license']} | {item['stars']} | "
            f"{item['pushed_at'][:10]} | {', '.join(notes) or '-'} |"
        )
    lines += ["", "## Candidate Discovery", "", "Candidates are not recommendations. A candidate needs manual review before README inclusion.", "", "| Repository | Tier | Score | Stars | License | Description | Evidence |", "| --- | --- | ---: | ---: | --- | --- | --- |"]
    seen: set[str] = set()
    existing = {item["repo"].lower() for item in inventory}
    ranked: list[tuple[int, int, dict, list[str]]] = []
    for item in candidates:
        repo = item.get("repo")
        if not repo or repo.lower() in seen or repo.lower() in existing:
            continue
        if item.get("state") == "unverified":
            lines.append(f"| - | review | 0 | - | - | API error | `{item.get('error', '')}` |")
            continue
        score, reasons = candidate_score(item, now)
        if score == 0:
            continue
        seen.add(repo.lower())
        ranked.append((score, item.get("stars", 0), item, reasons))
    for score, _, item, reasons in sorted(ranked, key=lambda row: (row[0], row[1]), reverse=True)[:25]:
        repo = item["repo"]
        tier = "A" if score >= 9 and item["stars"] >= 10 and item["license"] != "UNDECLARED" else "B" if score >= 8 else "review"
        evidence = ", ".join(reasons).replace("|", "\\|")
        description = item["description"].replace("|", "\\|").replace("\n", " ")[:120]
        lines.append(f"| [{repo}]({item['html_url']}) | {tier} | {score} | {item['stars']} | {item['license']} | {description} | {evidence}; pushed {item['pushed_at'][:10]} |")
    lines += ["", "## Quality Gate", "", "- Existing entries are metadata-checked only; no automatic README rewrite.", "- Archived, forked, inaccessible, or license-undeclared projects require review.", "- Candidate scores only prioritize review: topic match, license, adoption, activity, and description evidence.", "- New candidates are evidence leads, not automatic inclusions.", "- A human must approve the PR before `main` changes.", ""]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=REPORT)
    args = parser.parse_args()
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repos = [repo for _, repo in github_links(README.read_text(encoding="utf-8"))]
    with ThreadPoolExecutor(max_workers=8) as pool:
        inventory = list(pool.map(lambda repo: repo_status(repo, token), repos))
        discovered = list(pool.map(lambda query: discover(query, token), QUERIES))
    candidates = [item for group in discovered for item in group]
    now = datetime.now(timezone.utc)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(inventory, candidates, now), encoding="utf-8")
    print(f"wrote {args.output} ({len(inventory)} existing entries, {len(candidates)} candidate results)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
