---
type: Change
title: Repository AGENTS.md and worktree window titles
description: Added a rendered AGENTS.md, fixed the clink window title in git worktrees, and clarified the prepare-pr change file guidance.
tags:
  - agents
  - robotter
  - clink
  - worktree
  - skills
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-02T11:07:11-04:00
sources:
  - id: agents-md
    resource: /AGENTS.md
  - id: python-development
    resource: /robotter/python_development.jinja2.md
  - id: clink-prompt
    resource: /Windows/clink/my_agnoster.clinkprompt
  - id: prepare-pr-skill
    resource: /robotter/skills/prepare-pr/SKILL.md
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
---

# Summary

Adds an `AGENTS.md` to the repository root, fixes the console window title that the clink prompt
sets when the current directory is inside a git worktree, and tightens the wording of the
`prepare-pr` skill's change file step.

# Changes

## AGENTS.md

- Added `AGENTS.md`, rendered from `robotter/python_development.jinja2.md` (version marker
  `python_development Version: 0.8.0`).[^agents-md][^python-development] It carries the file format,
  architecture, documentation, linting, and Python conventions.

## clink prompt

- The window title is derived from `git.getgitdir()` by matching `<repo>\.git`.[^clink-prompt] In a
  worktree the git directory is `<repo>\.git\worktrees\<name>`, so the match returned `nil` and the
  following `gsub` call failed.
- Added two fallbacks: the worktree name for `\.git\worktrees\<name>` paths, then the last path
  component, then the raw git directory.

## prepare-pr skill

- Step 4 now says "no more than five questions" instead of "up to 5 questions".[^prepare-pr-skill]
- Step 4 now directs agents to favor compliance with the OKF format over conformance with existing
  change files, so errors in earlier change files are not copied forward.[^okf-spec]

# Rationale

Agents working in this repository previously had no repository-level instructions. `AGENTS.md`
applies the same conventions that robotter installs for other projects. The clink fix is needed
because worktrees are now part of the workflow (the `create-worktree` skill) and opening a prompt in
one broke title handling. The `prepare-pr` wording change makes OKF, not earlier output, the
reference for change files.

[^agents-md]: AGENTS.md
[^python-development]: robotter python_development template
[^clink-prompt]: clink agnoster prompt
[^prepare-pr-skill]: prepare-pr skill
[^okf-spec]: Open Knowledge Format v0.2 specification
