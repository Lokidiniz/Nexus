#!/usr/bin/env python3
"""
NEXUS Reference Guard Hook
Runs after Write/Edit tool calls to detect invalid reference placeholders.

Constitution Article I.1: No fabricated references.
"""

import sys
import re
import json

VIOLATIONS = []

# Patterns that indicate fake or incomplete references
FAKE_REF_PATTERNS = [
    # Generic numbered placeholders without description
    (r'\[(\d+)\](?!\s*[A-Z])', "Generic numbered placeholder [N] without author/year"),
    # Author placeholders
    (r'\[Author[,\s]+\d{4}\]', "Placeholder author citation"),
    (r'\(Author[,\s]+\d{4}\)', "Placeholder author citation"),
    # Generic ref tags
    (r'\[REF\](?!\s*NEEDED)', "Generic [REF] without description"),
    (r'\[CITATION NEEDED\]', "Citation needed marker — add description"),
    # Invented DOI patterns
    (r'doi:\s*10\.\d{4}/fake', "Likely fabricated DOI"),
    (r'doi:\s*10\.\d{4}/placeholder', "Placeholder DOI"),
]

# Patterns that are ALLOWED (properly marked incomplete refs)
ALLOWED_PATTERNS = [
    r'\[REF NEEDED:',           # Properly described missing ref
    r'\[revisar/confirmar ref\]',  # Review flag
    r'\[verify/confirm ref\]',
    r'\[verificar ref\]',
]

def check_content(content):
    """Check content for reference violations."""
    lines = content.split('\n')

    for line_num, line in enumerate(lines, 1):
        # Skip allowed patterns
        if any(re.search(p, line, re.IGNORECASE) for p in ALLOWED_PATTERNS):
            continue

        # Check for violations
        for pattern, description in FAKE_REF_PATTERNS:
            matches = re.findall(pattern, line, re.IGNORECASE)
            if matches:
                VIOLATIONS.append({
                    "line": line_num,
                    "content": line.strip(),
                    "issue": description,
                    "matches": matches
                })

def main():
    """Main hook entry point."""
    # Read from stdin (Claude Code passes tool output via stdin)
    try:
        if len(sys.argv) > 1:
            try:
                with open(sys.argv[1], 'r', encoding='utf-8') as f:
                    content = f.read()
            except (FileNotFoundError, IOError):
                content = sys.stdin.read()
        else:
            content = sys.stdin.read()
    except Exception:
        sys.exit(0)  # Don't block if we can't read

    if not content:
        sys.exit(0)

    check_content(content)

    if VIOLATIONS:
        print("\n" + "="*60)
        print("⚠️  NEXUS REFERENCE GUARD — Constitution Article I.1")
        print("="*60)
        print(f"Found {len(VIOLATIONS)} potential reference violation(s):\n")

        for v in VIOLATIONS:
            print(f"  Line {v['line']}: {v['issue']}")
            print(f"  Content: {v['content'][:80]}...")
            print()

        print("REQUIRED ACTION:")
        print("  Replace each [N] placeholder with either:")
        print("  → A real citation: (Author et al., Year) | DOI: 10.XXXX/XXXXX")
        print("  → A proper marker: [REF NEEDED: describe what to search for]")
        print()
        print("Constitution: 'No agent may generate citations from memory alone.'")
        print("="*60 + "\n")

        # Exit code 2 = warning (doesn't block, but alerts)
        # Change to sys.exit(1) to make it blocking
        sys.exit(2)

    sys.exit(0)

if __name__ == "__main__":
    main()
