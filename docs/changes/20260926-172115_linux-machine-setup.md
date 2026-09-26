---
type: Change
title: Linux machine setup
description: Adapted the dotfiles configuration so it can provision a Linux machine in addition to Windows.
tags:
  - linux
  - git
  - gpg
  - tuxedo
  - lazygit
  - uv
status: stable
generated:
  by: claude-code/claude-opus-5-5
  at: 2026-09-26T17:21:15-04:00
sources:
  - id: generic-yaml
    resource: /Generic/generic.yaml
  - id: gpg-script
    resource: /Generic/git/generate_git_gpg_key.sh
  - id: windows-yaml
    resource: /Windows/windows.yaml
  - id: lazygit-config
    resource: /Generic/lazygit/config.yml
---

# Summary

The configuration previously assumed a Windows environment in several places. This change makes the
generic configuration usable on Linux and moves Windows-specific entries into the Windows
configuration.

# Changes

## git

- Added a `git configuration` entry to `Generic/generic.yaml` that sets global defaults on every
  platform: `core.autocrlf false`, `tag.forceSignAnnotated true`, `init.defaultBranch main`,
  `pull.rebase true`, and `fetch.prune true`.
- Added `Generic/git/generate_git_gpg_key.sh`, run on non-Windows systems. It creates a
  non-expiring, passphrase-less GPG signing key (default `ed25519`) from the configured git
  `user.name`/`user.email` (overridable via `GIT_GPG_NAME`, `GIT_GPG_EMAIL`, `GIT_GPG_ALGO`), then
  sets `user.signingkey`, `commit.gpgsign`, and `tag.gpgsign`. It is idempotent: if a signing key is
  already configured, it verifies the key exists and exits; a configured key missing from the
  keyring is an error rather than being silently replaced.
- Added post-install instructions for settings that cannot be automated: `gpg.program` and
  per-directory `[includeIf]` includes for employer-specific identities.

## Executables on Linux

- `just/run` and `tux` are now installed to `~/.local/bin` with `make_executable: true` on
  non-Windows systems, so they are on `PATH` without additional configuration.

## tuxedo wrapper

- Renamed the wrapper scripts from `tuxedo` / `tuxedo.cmd` to `tux` / `tux.cmd`, and the wrappers
  now invoke the `tuxedo` executable directly instead of `_tuxedo`.
- Reason: on Linux, a wrapper script named `tuxedo` conflicted with the `tuxedo` executable of the
  same name. Windows was unaffected because the two files had different extensions.

## lazygit

- Replaced `git.pagers[].externalDiffCommand` with `git.diffRenderers[]` (`type: extDiff`) to follow
  the lazygit configuration schema change. The `difft` side-by-side behavior is unchanged.

## uv

- Moved `uv.env` from `Generic/` to `Windows/` and its entry to `Windows/windows.yaml`. The file is
  only needed for the Windows tools directory layout; Linux uses uv defaults.

# Rationale

The goal is to provision a Linux machine from the same dotfiles repository. Each change either
removes a Windows-only assumption from the generic configuration, resolves a name collision that
only surfaces on Linux, or automates setup (git defaults, commit signing) that was previously done
by hand.
