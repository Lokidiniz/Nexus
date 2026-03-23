#!/usr/bin/env bash
# NEXUS Hooks Installer
# Copies hooks to the target project directory

set -e

TARGET="${1:-.}"
NEXUS_HOOKS_DIR="$(dirname "$0")"

echo "Installing NEXUS hooks to: $TARGET"

mkdir -p "$TARGET/.nexus/hooks"
mkdir -p "$TARGET/.claude"

# Copy hooks
cp "$NEXUS_HOOKS_DIR/reference-guard.py" "$TARGET/.nexus/hooks/"
cp "$NEXUS_HOOKS_DIR/constitution-enforcer.py" "$TARGET/.nexus/hooks/"

# Copy settings if not already present
if [ ! -f "$TARGET/.claude/settings.json" ]; then
    cp "$(dirname "$NEXUS_HOOKS_DIR")/../.claude/settings.json" "$TARGET/.claude/"
    echo "  ✓ settings.json installed"
else
    echo "  ℹ️  settings.json already exists — skipping (merge manually if needed)"
fi

echo "  ✓ reference-guard.py installed"
echo "  ✓ constitution-enforcer.py installed"
echo ""
echo "Hooks active. They run automatically in Claude Code."
