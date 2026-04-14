#!/usr/bin/env python3

from __future__ import annotations

import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"
KERNEL_YAML = ROOT / "SESSION_KERNEL.yaml"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Missing required file: {path}")
    except yaml.YAMLError as exc:
        fail(f"Invalid YAML in {path}: {exc}")


def parse_skill_frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter.")

    parts = text.split("---\n", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is incomplete.")

    frontmatter = yaml.safe_load(parts[1])
    if not isinstance(frontmatter, dict):
        fail("SKILL.md frontmatter must parse to a mapping.")
    return frontmatter


def expect_keys(mapping: dict[str, object], keys: list[str], label: str) -> None:
    missing = [key for key in keys if key not in mapping]
    if missing:
        fail(f"{label} is missing required keys: {', '.join(missing)}")


def main() -> None:
    skill_meta = parse_skill_frontmatter(SKILL_MD)
    expect_keys(skill_meta, ["name", "description"], "SKILL.md frontmatter")
    if skill_meta["name"] != "session-kernel":
        fail("SKILL.md frontmatter name must be 'session-kernel'.")

    description = str(skill_meta["description"])
    if "Do not use for ordinary feature work" not in description:
        fail("SKILL.md description must preserve the narrow-trigger guardrail.")

    openai = load_yaml(OPENAI_YAML)
    if not isinstance(openai, dict):
        fail("agents/openai.yaml must parse to a mapping.")
    expect_keys(openai, ["interface", "policy"], "agents/openai.yaml")

    interface = openai["interface"]
    policy = openai["policy"]
    if not isinstance(interface, dict):
        fail("agents/openai.yaml interface must be a mapping.")
    if not isinstance(policy, dict):
        fail("agents/openai.yaml policy must be a mapping.")

    expect_keys(interface, ["display_name", "short_description", "default_prompt"], "agents/openai.yaml interface")
    if "$session-kernel" not in str(interface["default_prompt"]):
        fail("agents/openai.yaml default_prompt must explicitly mention $session-kernel.")
    if policy.get("allow_implicit_invocation") is not False:
        fail("agents/openai.yaml must keep allow_implicit_invocation set to false.")

    kernel = load_yaml(KERNEL_YAML)
    if not isinstance(kernel, dict):
        fail("SESSION_KERNEL.yaml must parse to a mapping.")
    expect_keys(
        kernel,
        [
            "version",
            "name",
            "scope",
            "project_discovery",
            "session_start_checklist",
            "work_execution_policy",
            "session_close_checklist",
            "agent_interpretation_rules",
        ],
        "SESSION_KERNEL.yaml",
    )

    print("session-kernel repository is valid.")


if __name__ == "__main__":
    main()
