#!/usr/bin/env python3
"""
NEXUS Constitution Enforcer Hook
Checks outputs against the NEXUS Constitution principles.

Runs as PreToolUse hook to flag potential violations before delivery.
"""

import sys
import re

WARNINGS = []

# Article I.2 — No invented data
DATA_FABRICATION_PATTERNS = [
    (r'LOD\s*=\s*0\.\d+\s*[nμm]M(?!\s*\(calculated)', "LOD value without calculation basis"),
    (r'R²\s*=\s*0\.9\d+(?!\s*\(from)', "R² value without source data"),
    (r'n\s*=\s*\d+(?!\s*participants|\s*replicates|\s*samples|\s*measurements)',
     "Sample size without context"),
]

# Article V.3 — No overpromising
OVERPROMISE_PATTERNS = [
    (r'\bproves?\b(?!\s+that\s+[a-z])', "Avoid 'proves' — prefer 'demonstrates' or 'suggests'"),
    (r'\bdecisvely\b', "Avoid 'decisively' without strong evidence basis"),
    (r'\bwithout\s+doubt\b', "Avoid 'without doubt' in scientific text"),
    (r'\bconclusively\s+shows?\b', "Prefer 'indicates' or 'suggests' unless evidence is overwhelming"),
    (r'\bperfect\b(?!\s+match|\s+fit)', "Avoid 'perfect' as scientific descriptor"),
]

# Article II.2 — Silent assumptions
SILENT_ASSUMPTION_PATTERNS = [
    (r'assuming\s+that\b(?!.*\[)', "Assumption declared but not flagged with [ASSUMED]"),
]

def check_for_violations(content):
    """Check content for constitution violations."""
    lines = content.split('\n')

    for line_num, line in enumerate(lines, 1):
        # Check data fabrication
        for pattern, msg in DATA_FABRICATION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                WARNINGS.append({
                    "article": "I.2",
                    "principle": "No invented data",
                    "line": line_num,
                    "issue": msg,
                    "content": line.strip()[:80]
                })

        # Check overpromising
        for pattern, msg in OVERPROMISE_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                WARNINGS.append({
                    "article": "V.3",
                    "principle": "No overpromising",
                    "line": line_num,
                    "issue": msg,
                    "content": line.strip()[:80]
                })

def main():
    try:
        content = sys.stdin.read()
    except Exception:
        sys.exit(0)

    if not content:
        sys.exit(0)

    check_for_violations(content)

    if WARNINGS:
        print("\n" + "="*60)
        print("📋 NEXUS CONSTITUTION CHECK")
        print("="*60)

        for w in WARNINGS:
            print(f"\n  ⚠️  Article {w['article']} — {w['principle']}")
            print(f"  Issue: {w['issue']}")
            print(f"  Line {w['line']}: {w['content']}")

        print("\n" + "="*60 + "\n")
        sys.exit(2)  # Warning, non-blocking

    sys.exit(0)

if __name__ == "__main__":
    main()
