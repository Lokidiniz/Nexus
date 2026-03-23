#!/usr/bin/env python3
"""Validate NEXUS task files."""

import os
import sys

TASKS_DIR = "tasks"
REQUIRED_SECTIONS = ["RDS Check", "Output Format"]

errors = []
warnings = []

task_files = [f for f in os.listdir(TASKS_DIR) if f.endswith(".md")]

if not task_files:
    print("ERROR: No task files found in tasks/")
    sys.exit(1)

for filename in sorted(task_files):
    path = os.path.join(TASKS_DIR, filename)

    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Check forbidden placeholder
    if "[N]" in content:
        errors.append(f"{filename}: Contains forbidden [N] placeholder")

    # Check recommended sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            warnings.append(f"{filename}: Missing recommended section '{section}'")

    # Check has a command reference
    if "Command:" not in content and "command:" not in content.lower():
        warnings.append(f"{filename}: No command reference found")

    print(f"  OK  {filename}")

print()
if warnings:
    for w in warnings:
        print(f"  WARN  {w}")

if errors:
    print()
    for e in errors:
        print(f"  ERROR  {e}")
    print(f"\n{len(errors)} error(s). Fix before merging.")
    sys.exit(1)

print(f"Validated {len(task_files)} task(s). {len(warnings)} warning(s). All OK.")
