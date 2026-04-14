---
name: session-kernel
description: Establish, audit, or update a project's workflow canon, session-start/session-close checklists, tool-selection rules, test discipline, VCS/publication rules, and durable runbooks. Use when Codex is asked to create or maintain reusable workflow documentation, consolidate working knowledge from prior sessions, or build a project-agnostic session kernel that can be reused across repositories. Do not use for ordinary feature work, debugging, code review, or generic documentation tasks unless the request is specifically about workflow canon or reusable session rules.
---

# Session Kernel

Use this skill to turn session knowledge into durable operating documentation.

Read [SESSION_KERNEL.yaml](SESSION_KERNEL.yaml) when a reusable machine-readable template is needed. Prefer project-local canon over the global template when the project already has stronger rules.

## Decision Gate

Use this skill only if the request is about one or more of the following:

- establishing a repeatable session workflow for a project
- auditing an existing workflow canon against actual repo behavior
- capturing tool rules, test rules, or publication rules into durable docs
- converting prior-session knowledge into project docs or a reusable kernel
- creating machine-readable session start or session close checklists

Do not use this skill when the task is simply to ship code, debug a bug, review a PR, or answer a normal product question.

## Workflow

1. Inspect project reality before writing canon.
Run repo-state commands, find source-of-truth docs, identify test layers, find CI or runtime entrypoints, and confirm the publication path.

2. Prefer project-local truth over memory.
Read the project's own README, docs, testing docs, runbooks, and existing canon before applying the global template.

3. Build or update the canon around observed reality.
Capture source-of-truth documents, workflow order, tool selection, fallbacks, test discipline, VCS/publication rules, known wrong paths, and any required machine-readable checklists.

4. Keep code, tests, docs, and canon aligned.
If behavior changes, update the relevant docs in the same slice. Do not leave new workflow knowledge only in chat history.

5. Prefer small durable artifacts.
Use concise project-local canon files, cross-link them from the repo's main docs, and add machine-readable YAML only when the user wants structured reuse.

6. Record capability gaps explicitly.
If a tool that existed in a prior session is unavailable in the current session, note the gap and document the fallback instead of pretending the capability exists.

## Preferred Outputs

Write project-local canon into the smallest durable set of files that fits the repo. Typical targets:

- `testing/tooling-canon.md`
- `docs/tooling-canon.md`
- `docs/project-canon.md`
- `testing/session-checklists.yaml`
- cross-links from `README.md` or other top-level operator docs

If the project has no good target, create one canonical doc and link it from the repo entrypoints.

## Validation

Before closing the slice:

- run the relevant deterministic tests
- verify docs reflect the shipped behavior
- inspect `git status --short` and `git diff --stat`
- commit code, tests, and docs together when the user wants history or publication
- push when publication is expected and allowed

## Reference Usage

Read [SESSION_KERNEL.yaml](SESSION_KERNEL.yaml) when:

- the project has no workflow canon yet
- the user wants a project-agnostic machine-readable template
- a new repo needs a bootstrap structure for session start, execution, and close rules

Do not copy the template blindly. Adapt it to the repo after discovery.

## Output Standard

Prefer concise, structured outputs that clearly separate:

- current repo reality
- chosen canon files
- workflow rules added or changed
- validation performed
- remaining gaps or follow-up items
