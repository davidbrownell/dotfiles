---
name: code-review
description: Perform systematic code reviews on files, diffs, PRs, or snippets. Use when the user asks to review code, check a PR, audit a change, find bugs/security issues, or requests a code review. Triggers include review this code, review the PR, code review, audit this change, check for bugs, security review.
metadata:
    version: 0.1.0
---

# Code Review

## Overview

Perform structured, high-signal code reviews that prioritize correctness, security, and maintainability. Focus on findings that matter; avoid style nitpicks already covered by linters.

## Workflow

1. **Gather context**
    - Identify the change scope (files, diff, PR description, linked issues).
    - Read related files, types, callers, and tests when the change is non-trivial.
    - Note the language, framework, and any project conventions if visible.

2. **Review in priority order**
    - Correctness and logic
    - Security and data safety
    - Error handling and edge cases
    - Performance and resource use
    - Tests and observability
    - Design and maintainability

3. **Produce findings**
    - Rank by severity: Critical > High > Medium > Low / Suggestion
    - Cite file and line (or approximate location) for every finding
    - Explain the risk and suggest a concrete fix
    - Deduplicate overlapping issues

4. **Summarize**
    - One-paragraph overall assessment
    - List of findings grouped by severity
    - Optional residual risks or follow-up questions

## Review Checklist

### Correctness
- Does the change implement the stated intent and nothing else?
- Are boundary conditions handled (null/None, empty, zero, negative, max values, off-by-one)?
- Are concurrent or async paths free of race conditions and ordering bugs?
- Do types, interfaces, and contracts still hold after the change?
- Are there dead or unreachable paths introduced?

### Security
- No hardcoded secrets, keys, tokens, or credentials
- User or external input is validated/sanitized at trust boundaries
- Queries and commands use parameterization or safe APIs (no string concatenation)
- Authorization checks exist beyond mere authentication (IDOR, ownership, role)
- Sensitive data is not logged, returned in errors, or exposed in responses
- Crypto uses modern primitives and correct modes; no weak hashes or ECB
- Path handling prevents traversal; redirects and URLs are validated

### Error Handling and Resilience
- Errors are handled specifically, not swallowed by bare catch/except
- Failures propagate or are recovered with clear semantics
- Timeouts, retries, and cancellation are considered where I/O occurs
- Resource cleanup (files, connections, locks) happens on all paths

### Performance
- No obvious N+1 queries or repeated work in loops
- Hot paths avoid unnecessary allocations or quadratic algorithms
- Large payloads or unbounded collections are guarded
- Caching or batching is used only when justified and correct

### Tests
- New behavior has corresponding tests (or a clear reason why not)
- Tests assert real behavior, not just mock interactions
- Edge cases and failure modes are covered
- Tests would fail if the production change were removed

### Design and Maintainability
- Follows existing project patterns and layering
- Naming is clear and consistent
- No premature abstractions or speculative generality
- No leaky or misplaced responsibility
- Comments explain why, not what
- Public APIs and breaking changes are intentional and documented
- Code is not duplicated

## Output Format

```
# Code Review Summary

[1-3 sentence overall verdict and main risks]

## Critical
- **Issue title**
  path/to/file:line
  Risk: …
  Fix: …

## High
…

## Medium
…

## Low / Suggestions
…

## Residual Questions
```

If no issues are found, state that clearly and note any residual risks or areas that still need human judgment (architecture, product intent, etc.).

## Principles

- Prefer high-signal findings over exhaustive style commentary.
- Assume AI-generated code may miss cross-cutting updates and produce weak tests — verify both.
- Do not rewrite large sections unless the user asks for fixes; report first.
- When the language or framework is clear, apply its idiomatic safety rules.
- If context is missing (full repo, tests, config), say what you could not verify.

## Anti-Patterns to Avoid

- Do not invent problems to appear thorough.
- Do not restate what the code does as if it were a finding.
- Do not soften a defect to be agreeable, and do not inflate a nit to seem rigorous.
- Do not approve code that you did not actually read.
