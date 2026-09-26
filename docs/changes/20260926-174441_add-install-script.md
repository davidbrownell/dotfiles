---
type: Change
title: Install script and skill directory layout
description: Added a single install script and adapted the repository to breaking changes in dbrownell_Dotter and robotter.
tags:
  - install
  - dotter
  - robotter
  - skills
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-09-26T17:44:41-04:00
sources:
  - id: install-script
    resource: /install.py
  - id: windows-yaml
    resource: /Windows/windows.yaml
  - id: readme
    resource: /README.md
  - id: robotter-readme
    resource: /robotter/README.md
  - id: python-development
    resource: /robotter/python_development.jinja2.md
  - id: code-review-skill
    resource: /robotter/skills/code-review
  - id: create-worktree-skill
    resource: /robotter/skills/create-worktree/SKILL.md
  - id: prepare-pr-skill
    resource: /robotter/skills/prepare-pr/SKILL.md
  - id: understand-code-skill
    resource: /robotter/skills/understand-code/SKILL.md
---

# Summary

Installing the dotfiles previously required running `dbrownell_Dotter` and `robotter` by hand with
the correct arguments. This change adds `install.py`, which runs both, and updates the repository to
match breaking changes in both tools.

# Changes

## install.py

- Added `install.py`, a `uv run --script` entry point (dependency: `typer`) that takes a
  `tools_dir` argument and optional `--force` and `--force-symbolic-links` flags.
- It runs `uvx dbrownell_Dotter Install` with `Generic/generic.yaml`, plus `Windows/windows.yaml`
  when running on Windows, passing `tools_dir` as a variable.
- It then runs `uvx robotter render_skill <skill> claude-code` for every directory under
  `robotter/skills`.
- A failing command stops the script and returns that command's exit code.

## dbrownell_Dotter

- Removed `source: null` from the `clink_settings` entry in `Windows/windows.yaml`. A breaking
  change in dbrownell_Dotter made that syntax invalid. An entry that only applies substitutions to
  an existing destination now leaves out `source`.

## robotter templates

- Templates are now identified explicitly (by the `.jinja2.md` extension) and only those files are
  rendered. Renamed `python_development.md` to `python_development.jinja2.md` because it uses
  `include_configuration`. Its version marker changed to `python_development Version: 0.8.0`.
- Removed the `{% raw %}` / `{% endraw %}` escapes from `skills/code-review`. Those files are not
  templates. They were escaped only because they contain `{{…}}` placeholder syntax, and they are no
  longer rendered.

## Skills

- Moved every skill into its own directory containing a `SKILL.md`, so `install.py` can find all
  skills by listing directories: `create_worktree.md` → `create-worktree/`, `understand_code.md` →
  `understand-code/`, `prepare_branch.md` → `prepare-pr/`.
- Renamed the `prepare-branch` skill to `prepare-pr`. It has two new steps. The first generates a
  slug from the changes and uses it as the branch name. The second writes an OKF change file to
  `docs/changes/<datetime>_<slug>.md` before squashing. The commit message is now built from that
  change file: one paragraph on what changed, one on why.

## Documentation

- Fixed the top-level `README.md`, which listed the `robotter` command as `uvx dotter`.
- Updated `robotter/README.md` for the `.jinja2.md` rename. Removed the single-file skill examples,
  since no single-file skills remain.
- Normalized line endings in `robotter/README.md` and the `prepare-pr` skill.

# Rationale

The goal is a single command that installs the whole configuration on a machine. Other changes were
required because dbrownell_Dotter and robotter both introduced breaking changes: without them,
installation fails (`source: null`) or skill files would be handled incorrectly. Putting every skill
in its own directory means `install.py` can render them all without keeping a list of skills.
