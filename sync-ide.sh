#!/usr/bin/env bash
# sync-ide.sh — NEXUS Academic Research Framework
# Sync agents and configs across Claude Code, Cursor, and Gemini CLI
# Usage: bash sync-ide.sh [--force]

set -e

NEXUS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FORCE=false

for arg in "$@"; do
  [[ "$arg" == "--force" || "$arg" == "-f" ]] && FORCE=true
done

# ─── Colors ──────────────────────────────────────────────────────────────────

GREEN='\033[0;32m'; CYAN='\033[0;36m'; YELLOW='\033[1;33m'
RED='\033[0;31m'; BOLD='\033[1m'; RESET='\033[0m'

ok()   { echo -e "  ${GREEN}✓${RESET} $1"; }
info() { echo -e "  ${CYAN}→${RESET} $1"; }
warn() { echo -e "  ${YELLOW}⚠${RESET} $1"; }
err()  { echo -e "  ${RED}✗${RESET} $1"; }

# ─── Banner ──────────────────────────────────────────────────────────────────

echo ""
echo -e "${BOLD}NEXUS — IDE Sync${RESET}"
echo -e "${CYAN}Syncing agents across Claude Code · Cursor · Gemini CLI${RESET}"
echo ""

# ─── Detect home directory ───────────────────────────────────────────────────

if [[ -n "$USERPROFILE" ]]; then
  HOME_DIR="$USERPROFILE"   # Windows via Git Bash
else
  HOME_DIR="$HOME"          # Unix/macOS
fi

# ─── 1. Claude Code (global agents) ─────────────────────────────────────────

CLAUDE_DIR="$HOME_DIR/.claude"
CLAUDE_AGENTS="$CLAUDE_DIR/agents"

info "Claude Code: $CLAUDE_AGENTS"

if [[ -d "$CLAUDE_DIR" ]]; then
  mkdir -p "$CLAUDE_AGENTS"
  count=0
  for agent in "$NEXUS_DIR/agents/"*.md; do
    name=$(basename "$agent")
    dest="$CLAUDE_AGENTS/$name"
    if [[ ! -f "$dest" || "$FORCE" == true ]]; then
      cp "$agent" "$dest"
      ((count++))
    fi
  done

  # Sync CLAUDE.md (global activation)
  src_claude="$NEXUS_DIR/.claude/CLAUDE.md"
  dst_claude="$CLAUDE_DIR/CLAUDE.md"
  if [[ -f "$src_claude" && (! -f "$dst_claude" || "$FORCE" == true) ]]; then
    cp "$src_claude" "$dst_claude"
    ok "CLAUDE.md → $dst_claude"
  fi

  ok "Agents synced: $count files → $CLAUDE_AGENTS"
else
  warn "Claude Code not found at $CLAUDE_DIR (skip)"
fi

# ─── 2. Cursor ───────────────────────────────────────────────────────────────

CURSOR_RULES="$NEXUS_DIR/.cursor/rules"
CURSOR_SRC="$NEXUS_DIR/.cursor/rules/nexus.mdc"

info "Cursor: $CURSOR_RULES"

if [[ -f "$CURSOR_SRC" ]]; then
  ok "Cursor rules present at $CURSOR_RULES"
else
  mkdir -p "$CURSOR_RULES"
  warn "nexus.mdc missing — re-run after Phase 2 or check .cursor/rules/"
fi

# ─── 3. Gemini CLI ───────────────────────────────────────────────────────────

GEMINI_SRC="$NEXUS_DIR/.gemini/GEMINI.md"

info "Gemini CLI: $NEXUS_DIR/.gemini/"

if [[ -f "$GEMINI_SRC" ]]; then
  ok "GEMINI.md present at $GEMINI_SRC"
else
  warn "GEMINI.md missing — re-run after Phase 2"
fi

# ─── 4. NEXUS internal (.nexus/) ─────────────────────────────────────────────

NEXUS_INTERNAL="$NEXUS_DIR/.nexus"
info "NEXUS internals: $NEXUS_INTERNAL"

for f in constitution.md activation-pipeline.md rds.md; do
  if [[ -f "$NEXUS_INTERNAL/$f" ]]; then
    ok "  $f"
  else
    warn "  $f MISSING"
  fi
done

# ─── 5. Summary ──────────────────────────────────────────────────────────────

echo ""
echo -e "${BOLD}Sync complete.${RESET}"
echo ""
echo "  To force overwrite existing files: bash sync-ide.sh --force"
echo "  To install fresh in a new project: npx nexus-research init"
echo ""
