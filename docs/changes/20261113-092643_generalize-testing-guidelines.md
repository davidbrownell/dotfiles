---
type: Change
title: Generalize testing guidelines across all languages
description: Moved language-agnostic testing principles from the Python guidelines into the shared development guidelines and added rules for distinct test coverage and shared setup.
tags:
  - robotter
  - agents
  - testing
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-11-13T09:26:43-05:00
sources:
  - id: all-development
    resource: /robotter/all_development.md
  - id: python-development
    resource: /robotter/python_development.jinja2.md
  - id: agents-md
    resource: /AGENTS.md
---

# Summary

Testing principles that apply regardless of language now live in the shared development
guidelines, and the Python guidelines retain only Python-specific testing conventions.[^all-development][^python-development]

# Changes

## robotter/all_development.md

- Added a `Testing` section containing: tests must exercise and validate functionality; each test
  must cover distinct behavior; repeated setup is extracted into fixtures or helpers; code is never
  removed to make tests pass; entire strings are compared when asserting equality.[^all-development]

## robotter/python_development.jinja2.md

- Bumped the version from 0.9.0 to 0.10.0.[^python-development]
- Removed the generic testing rules now inherited from `all_development.md` and scoped the section
  to Python tests.[^python-development]

## AGENTS.md

- Regenerated from the updated templates (version 0.10.0).[^agents-md]

# Rationale

The generic testing rules were only reachable through the Python guidelines, so agents working in
other languages did not receive them. Moving them to the shared file applies them everywhere. The
new rules on distinct coverage and fixture extraction discourage redundant tests and duplicated
setup.

[^all-development]: Shared development guidelines
[^python-development]: Python development guidelines template
[^agents-md]: Rendered repository agent instructions
