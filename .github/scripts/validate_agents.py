#!/usr/bin/env python3
"""Validate NEXUS agent frontmatter."""

import os
import sys
import yaml

REQUIRED_FIELDS = ["name", "description", "model"]
VALID_MODELS = ["haiku", "sonnet", "opus"]
VALID_COLORS = ["blue", "green", "red", "yellow", "purple", "orange", "cyan", None]
AGENTS_DIR = "agents"

errors = []
warnings = []

agent_files = [f for f in os.listdir(AGENTS_DIR) if f.endswith(".md")]

if not agent_files:
    print("ERROR: No agent files found in agents/")
    sys.exit(1)

for filename in sorted(agent_files):
    path = os.path.join(AGENTS_DIR, filename)

    with open(path, encoding="utf-8") as f:
        content = f.read()

    # Extract frontmatter
    if not content.startswith("---"):
        errors.append(f"{filename}: Missing frontmatter (file must start with ---)")
        continue

    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{filename}: Malformed frontmatter")
        continue

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        errors.append(f"{filename}: YAML parse error — {e}")
        continue

    if not isinstance(fm, dict):
        errors.append(f"{filename}: Frontmatter is not a mapping")
        continue

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"{filename}: Missing required field '{field}'")

    # model validation
    if "model" in fm and fm["model"] not in VALID_MODELS:
        errors.append(f"{filename}: Invalid model '{fm['model']}' — must be one of {VALID_MODELS}")

    # color validation
    if "color" in fm and fm["color"] not in VALID_COLORS:
        warnings.append(f"{filename}: Unusual color '{fm['color']}'")

    # commands array
    if "commands" in fm:
        if not isinstance(fm["commands"], list):
            errors.append(f"{filename}: 'commands' must be a list")
        else:
            for i, cmd in enumerate(fm["commands"]):
                if not isinstance(cmd, dict) or "name" not in cmd:
                    errors.append(f"{filename}: commands[{i}] missing 'name'")

    # Body must reference constitution
    body = parts[2]
    if "constitution" not in body.lower() and "activation-pipeline" not in body.lower():
        warnings.append(f"{filename}: Body does not reference constitution or activation-pipeline")

    print(f"  OK  {filename}")

print()
if warnings:
    for w in warnings:
        print(f"  WARN  {w}")

if errors:
    print()
    for e in errors:
        print(f"  ERROR  {e}")
    print(f"\n{len(errors)} error(s) found. Fix before merging.")
    sys.exit(1)

print(f"Validated {len(agent_files)} agent(s). {len(warnings)} warning(s). All OK.")
