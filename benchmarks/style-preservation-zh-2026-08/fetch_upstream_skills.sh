#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$ROOT/skills"
mkdir -p "$DEST"

curl -fsSL "https://raw.githubusercontent.com/blader/humanizer/523374dee72d67c7b2b5f858ea0094ffda49c3ac/SKILL.md" -o "$DEST/humanizer.SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/hardikpandya/stop-slop/8da1f030185bdfe8471220585162991eaeb970e9/SKILL.md" -o "$DEST/stop-slop.SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/conorbronsdon/avoid-ai-writing/d9fbca05a912aae8b35b56c92d132962c2cf4520/SKILL.md" -o "$DEST/avoid-ai-writing.SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/docwriter-org/plain-writing-skill/57a25d2fb8f3550ccab4c903438024b8d00125d9/SKILL.md" -o "$DEST/plain-writing.SKILL.md"
curl -fsSL "https://raw.githubusercontent.com/harshaneel/humanize/4ec797314537ec9c2105f276d4561d240a0390ba/humanize/SKILL.md" -o "$DEST/humanize.SKILL.md"

printf 'Fetched pinned SKILL.md snapshots into %s\n' "$DEST"
