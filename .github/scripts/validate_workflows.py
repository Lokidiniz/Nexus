#!/usr/bin/env python3
"""Validate NEXUS workflow YAML files."""

import os
import sys
import yaml

REQUIRED_FIELDS = ["name", "description", "phases"]
REQUIRED_PHASE_FIELDS = ["id", "name", "agent", "description"]
WORKFLOWS_DIR = "workflows"

errors = []

workflow_files = [f for f in os.listdir(WORKFLOWS_DIR) if f.endswith(".yaml")]

if not workflow_files:
    print("ERROR: No workflow files found in workflows/")
    sys.exit(1)

for filename in sorted(workflow_files):
    path = os.path.join(WORKFLOWS_DIR, filename)

    with open(path, encoding="utf-8") as f:
        try:
            wf = yaml.safe_load(f)
        except yaml.YAMLError as e:
            errors.append(f"{filename}: YAML parse error — {e}")
            continue

    if not isinstance(wf, dict):
        errors.append(f"{filename}: Not a valid YAML mapping")
        continue

    for field in REQUIRED_FIELDS:
        if field not in wf:
            errors.append(f"{filename}: Missing required field '{field}'")

    phases = wf.get("phases", [])
    if not isinstance(phases, list) or len(phases) == 0:
        errors.append(f"{filename}: 'phases' must be a non-empty list")
    else:
        for phase in phases:
            if not isinstance(phase, dict):
                errors.append(f"{filename}: phase is not a mapping")
                continue
            for pf in REQUIRED_PHASE_FIELDS:
                if pf not in phase:
                    errors.append(f"{filename}: phase {phase.get('id', '?')} missing '{pf}'")

    print(f"  OK  {filename}")

print()
if errors:
    for e in errors:
        print(f"  ERROR  {e}")
    print(f"\n{len(errors)} error(s) found.")
    sys.exit(1)

print(f"Validated {len(workflow_files)} workflow(s). All OK.")
