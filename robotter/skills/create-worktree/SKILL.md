---
name: create-worktree
description: Create a new git worktree as a sibling directory of the main repository, named `<repo-dir>_wt_<description>`, on a new branch off mainline, then run the project's setup so the worktree is immediately usable. Use when the user asks to create/add a worktree, spin up a worktree for a change, or work on something in a separate checkout.
metadata:
    version: 0.1.0
---

# Create Git Worktree

Add a git worktree beside the main repository for isolated work on a single change.

## 1. Determine the slug

The first argument is a very short description of the change (e.g. `json output`). If absent, derive one from the user's stated intent and confirm it; ask if intent is unclear.

Slugify to 2-3 words: lowercase, non-alphanumeric runs to single hyphens, ends stripped. `JSON Output!` becomes `json-output`.

## 2. Gather state

Stop and report if any check fails.

```bash
git rev-parse --is-inside-work-tree
ls .git/rebase-merge .git/rebase-apply .git/MERGE_HEAD   # must all be absent
git worktree list                                        # first entry is the main checkout
git remote show origin | grep 'HEAD branch'              # mainline branch
```

Use the main checkout path from `git worktree list`; `git rev-parse --show-toplevel` reports the worktree when run inside one. Determine mainline from `origin`'s HEAD, falling back to whichever of `main` or `master` exists locally. Do not assume `main`.

## 3. Compute the target path

The worktree is a sibling of the main repository directory: `<parent-of-repo-root>/<repo-dir-name>_wt_<slug>`. A repository at `E:\GitHub\gt-csse\RepoAuditorWeb` with slug `json-output` yields `E:\GitHub\gt-csse\RepoAuditorWeb_wt_json-output`.

Stop and report if that path already exists — never overwrite or reuse it.

## 4. Create the worktree

```bash
git worktree add -b <slug> <target-path> <mainline>
```

Branching from mainline rather than `HEAD` avoids carrying unrelated work. Mainline being checked out elsewhere is not a conflict.

If `<slug>` already exists as a branch this fails; stop and ask for a different description rather than reusing the branch or mangling the name.

## 5. Run project setup

Run in the new worktree, using the setup documented in `CLAUDE.md`, `CONTRIBUTING.md`, or `DEVELOPMENT.md` if present. Otherwise match on a marker file:

| Marker | Command |
| --- | --- |
| `uv.lock` | `uv sync` |
| `poetry.lock` | `poetry install` |
| `package-lock.json` | `npm ci` |
| `pnpm-lock.yaml` | `pnpm install` |
| `yarn.lock` | `yarn install` |
| `Cargo.toml` | `cargo fetch` |
| `go.mod` | `go mod download` |
| `.pre-commit-config.yaml` | `pre-commit install` |

No match: skip and say so. Failure is not fatal — the worktree is still usable, so report the output and let the user decide whether to retry.

## 6. Report

State the worktree path, new branch, base branch, and setup result.

## 7. Start editing

Open an IDE in the new worktree.