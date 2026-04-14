# Contributing

Thanks for contributing to `session-kernel`.

The repository is intentionally small. The goal is not to accumulate generic process advice, but to keep one sharp reusable skill plus one reusable machine-readable kernel.

## What Good Contributions Look Like

Good changes usually do one or more of the following:

- improve trigger precision so the skill is used less accidentally
- strengthen the workflow contract in `SESSION_KERNEL.yaml`
- improve the public explanation in `README.md`
- tighten the skill instructions in `SKILL.md`
- add or refine GitHub project scaffolding for public collaboration

## What To Avoid

Avoid changes that:

- broaden the skill into a generic coding assistant
- duplicate the same rule in too many places
- add project-specific assumptions into the universal kernel
- add long theory without changing actual behavior
- make implicit invocation more likely without a strong reason

## Change Rules

Keep changes small and intentional.

When behavior changes, update the matching files in the same slice:

- `SKILL.md` for trigger rules and usage guidance
- `SESSION_KERNEL.yaml` for machine-readable workflow rules
- `README.md` for public-facing explanation
- `agents/openai.yaml` if UI metadata or implicit invocation policy changes

## Validation

Before opening or updating a pull request:

1. Validate the skill structure if you have a Codex environment available.
2. Re-read the skill description and confirm it still has a narrow trigger.
3. Check that `SKILL.md`, `SESSION_KERNEL.yaml`, and `README.md` do not drift from each other.
4. Inspect the final diff and keep the scope coherent.

Example validator command in a Codex environment:

```bash
python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" /path/to/session-kernel
```

## Pull Requests

Open small pull requests with a clear reason for change.

A strong PR should explain:

- what changed
- why the previous behavior was not good enough
- whether trigger behavior changed
- whether the machine-readable kernel changed
- how the change was validated

## Discussions And Issues

Use GitHub Discussions for broad ideas and design questions.

Use GitHub Issues for:

- concrete bugs
- trigger mistakes
- documentation drift
- missing examples
- changes to the kernel structure
