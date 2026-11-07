---
type: Change
title: Render global agent configuration during install
description: Updated install.py to render robotter/global.md for claude-code so the global persona configuration is installed alongside skills.
tags:
  - robotter
  - install
  - configuration
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-11-07T15:55:48-05:00
sources:
  - id: install-script
    resource: /install.py
  - id: global-md
    resource: /robotter/global.md
  - id: robotter-readme
    resource: /robotter/README.md
---

# Summary

`install.py` now runs `robotter render global.md claude-code` before rendering skills, so the global
agent configuration is installed as part of the standard install.

# Changes

## install.py

- Added `robotter("render", "global.md", "claude-code")` to the robotter section, ahead of the loop
  that renders each directory under `robotter/skills`.[^install-script]

# Rationale

`robotter/global.md` defines the global persona (tone and framing rules) for the
agent,[^global-md] but the install script only rendered skills, so the file had to be rendered
manually with `uvx robotter render`.[^robotter-readme] Rendering it during install keeps the global
agent configuration in sync with the repository on every machine.

[^install-script]: dotfiles install script
[^global-md]: robotter global persona configuration
[^robotter-readme]: robotter usage documentation
