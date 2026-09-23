This directory contains files used with `https://github.com/davidbrownell/robotter`.

## Usage
- `uvx robotter render <template_filename> <agent_name> [output_dir]`
- `uvx robotter render_skill <template_filename> <agent_name> [output_dir]`

## Examples

| Example | Command Line |
| --- | --- |
| Global `CLAUDE.md` configuration | `uvx robotter render python_development.md claude-code` |
| Local `CLAUDE.md` configuration | `uvx robotter render python_development.md claude-code "<output_dir>"` |
| Global **Claude** skill (single file) | `uvx robotter render_skill skills/create_worktree.md claude-code` |
| Local **Claude** skill (single file) | `uvx robotter render_skill skills/create_worktree.md claude-code "<output_dir>"` |
| Global **Claude** skill (directory) | `uvx robotter render_skill skills/code-review claude-code` |
| Local **Claude** skill (directory) | `uvx robotter render_skill skills/code-review claude-code "<output_dir>"` |
