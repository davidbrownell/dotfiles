---
type: Change
title: Restrict change file generation to prepare-pr
description: Added a documentation rule that limits creation of files in docs/changes to the prepare-pr skill and bumped the python_development version marker.
tags:
  - robotter
  - documentation
  - skills
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-10-23T12:45:19-04:00
sources:
  - id: all-development
    resource: /robotter/all_development.md
  - id: python-development
    resource: /robotter/python_development.jinja2.md
  - id: prepare-pr-skill
    resource: /robotter/skills/prepare-pr/SKILL.md
---

# Summary

Adds a documentation rule stating that files in `docs/changes` are generated only by the
`prepare-pr` skill, and bumps the `python_development` template version so installed configurations
pick up the rule.

# Changes

## all_development.md

- Added to the Documentation section: "Do not generate files in `docs/changes` unless running the
  `prepare-pr` skill."[^all-development]

## python_development template

- Version marker changed from `python_development Version: 0.8.0` to
  `python_development Version: 0.9.0`.[^python-development] The template includes
  `all_development.md`, so the version change signals that rendered output differs.

# Rationale

Change files in `docs/changes` are produced by Step 4 of the `prepare-pr` skill, once per
branch.[^prepare-pr-skill] Agents doing ordinary development work could otherwise create change files
on their own, which duplicates or conflicts with the file `prepare-pr` writes when the branch is
squashed. The rule keeps a single owner for change files.

[^all-development]: robotter all_development guidance
[^python-development]: robotter python_development template
[^prepare-pr-skill]: prepare-pr skill
