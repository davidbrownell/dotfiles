---
type: Change
title: Resolve commit_emojis via uv run before PATH in prepare-pr
description: Updated the prepare-pr skill to invoke commit_emojis through `uv run` when available, falling back to the PATH-installed tool.
tags:
  - robotter
  - skills
  - prepare-pr
  - commit-emojis
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-11-09T16:14:54-05:00
sources:
  - id: prepare-pr-skill
    resource: /robotter/skills/prepare-pr/SKILL.md
---

# Summary

The prepare-pr skill now resolves the `commit_emojis` invocation at runtime, preferring
`uv run commit_emojis` and falling back to `commit_emojis` on `PATH`.[^prepare-pr-skill]

# Changes

## robotter/skills/prepare-pr/SKILL.md

- Replaced the `PATH`-only precondition with an ordered resolution: `uv run commit_emojis`
  (project dev dependency), then `commit_emojis` on `PATH`.[^prepare-pr-skill]
- Introduced the `<commit_emojis>` placeholder and used it in the `DisplayJson` and `Transform`
  commands.[^prepare-pr-skill]
- Removed the instruction that prohibited prefixing the command with `uv run`; `uvx` and hardcoded
  emoji lists remain prohibited.[^prepare-pr-skill]

# Rationale

The previous precondition required a machine-wide `commit_emojis` install and forbade `uv run`, so
the skill failed in environments where the tool is only available as a project dev dependency.
Preferring `uv run` uses the version pinned by the project when one exists, while the `PATH`
fallback preserves the existing behavior on machines with a global install.

[^prepare-pr-skill]: prepare-pr skill definition
