#!/usr/bin/env bash
# NEXUS v2.0 — Installer for Linux / macOS / WSL
# Usage: curl -fsSL <url>/install.sh | bash

set -e

REPO_URL="https://raw.githubusercontent.com/Lokidiniz/Nexus/main"
CLAUDE_DIR="$HOME/.claude"
AGENTS_DIR="$CLAUDE_DIR/agents"
SKILLS_DIR="$CLAUDE_DIR/skills"

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║   NEXUS v2.0 — Academic Research Squad Installer            ║"
echo "║   PT-BR · EN · ES  │  Claude Code                          ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Check Claude Code installation
if [ ! -d "$CLAUDE_DIR" ]; then
    echo "❌ Claude Code directory not found at $CLAUDE_DIR"
    echo "   Please install Claude Code first: https://claude.ai/code"
    exit 1
fi

# Create directories if needed
mkdir -p "$AGENTS_DIR"
mkdir -p "$SKILLS_DIR/nexus"
mkdir -p "$SKILLS_DIR/nexus-en"
mkdir -p "$SKILLS_DIR/nexus-es"

echo "📦 Installing NEXUS agents..."

AGENTS=(
    "nexus.md"
    "literature-researcher.md"
    "methodologist.md"
    "critical-analyst.md"
    "scientific-writer.md"
    "peer-reviewer.md"
    "data-specialist.md"
)

for agent in "${AGENTS[@]}"; do
    echo "   → $agent"
    curl -fsSL "$REPO_URL/agents/$agent" -o "$AGENTS_DIR/$agent"
done

echo ""
echo "📦 Installing NEXUS skills..."

SKILLS=("nexus" "nexus-en" "nexus-es")
for skill in "${SKILLS[@]}"; do
    echo "   → /nexus skill: $skill"
    curl -fsSL "$REPO_URL/skills/$skill/SKILL.md" -o "$SKILLS_DIR/$skill/SKILL.md"
done

echo ""
echo "✅ NEXUS v2.0 installed successfully!"
echo ""
echo "Usage in Claude Code:"
echo "   /nexus          — auto-detect language (PT-BR/EN/ES)"
echo "   /nexus-en       — English mode"
echo "   /nexus-es       — Español mode"
echo ""
echo "Example:"
echo "   /nexus revisão de literatura sobre sensores eletroquímicos com MOFs"
echo ""
