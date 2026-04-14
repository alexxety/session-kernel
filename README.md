# Session Kernel

`session-kernel` is a narrowly scoped Codex skill plus a machine-readable workflow template for building durable project operating canon.

It is meant for cases where a coding session should not rely on chat memory alone. The skill helps move working knowledge into persistent project docs, checklists, test rules, and publication rules.

## What This Repository Contains

- `SKILL.md`
  The skill contract and trigger rules for Codex.
- `SESSION_KERNEL.yaml`
  A project-agnostic machine-readable template for session start, execution, and close workflows.
- `agents/openai.yaml`
  Skill metadata with `allow_implicit_invocation: false`, so the skill is intended for explicit use rather than silent auto-invocation.

## When To Use It

Use `session-kernel` when you need to:

- establish a project workflow canon
- audit whether a repo's docs match how work actually happens
- create or update session-start and session-close checklists
- capture tool rules, test rules, or publication rules into durable docs
- turn prior-session knowledge into reusable project documentation

Do not use it for ordinary feature work, generic debugging, or normal code review unless the request is specifically about workflow canon or reusable session rules.

## How To Use The Skill

Invoke it explicitly:

```text
Use $session-kernel to audit this repo and build a workflow canon.
```

```text
Use $session-kernel to create session-start and session-close checklists for this project.
```

```text
Use $session-kernel to consolidate prior session knowledge into durable project docs.
```

## Installing The Skill Locally

Place this repository where you keep shared Codex assets, then link it into your Codex skills directory:

```bash
ln -s /path/to/session-kernel "${CODEX_HOME:-$HOME/.codex}/skills/session-kernel"
```

If a link already exists, replace it with the path to this repository.

## Typical Output Targets In A Project

The skill is designed to create or update a small set of durable project files, such as:

- `testing/tooling-canon.md`
- `docs/project-canon.md`
- `testing/session-checklists.yaml`
- cross-links from `README.md`

## Design Principles

- prefer project docs over memory
- prefer repository reality over assumptions
- prefer deterministic tests over manual confidence
- keep code, tests, docs, and git history aligned
- record missing tools or capability gaps explicitly

## License

This repository is released under the MIT License. See [LICENSE](LICENSE).

## Contributing

Contributions are welcome when they improve the skill without making it broader, noisier, or more likely to trigger accidentally.

Start with [CONTRIBUTING.md](CONTRIBUTING.md) for contribution rules and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation expectations.
