# Security Policy

## Scope

`session-kernel` is a documentation-heavy skill repository, not a deployed service. The main security concerns here are:

- malicious or unsafe workflow guidance
- accidental broadening of the skill trigger surface
- supply-chain risk introduced through future automation or dependencies
- disclosure of private operational details in examples or docs

## Supported Versions

Security fixes, if needed, should target:

- the latest `main`
- the latest published release

Older snapshots may not receive fixes.

## Reporting

For non-sensitive problems, open a normal GitHub issue.

For anything that should not be disclosed publicly, contact the repository owner privately through GitHub profile channels and include:

- a short summary
- the affected file or workflow
- why the issue matters
- any reproduction or evidence

Please avoid posting sensitive details in a public issue first.

## Response Expectations

This is a small maintained repository, not a staffed security program. Best effort expectations:

- acknowledgement when the report is seen
- clarification questions if the report is incomplete
- a fix or documented decision when the issue is confirmed and in scope

## Disclosure Guidance

Prefer responsible disclosure for issues that could:

- mislead users into unsafe workflow behavior
- leak private data through docs or examples
- introduce execution risk through automation or future CI changes
