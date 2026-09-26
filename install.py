#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = ["typer"]
# ///
"""Installs the dotfiles on the current machine."""

import subprocess
import sys
from pathlib import Path
from typing import Annotated

import typer


# ----------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent
ROBOTTER_DIR = REPO_ROOT / "robotter"


# ----------------------------------------------------------------------
app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    pretty_exceptions_show_locals=False,
)


# ----------------------------------------------------------------------
def run(command: list[str | Path], cwd: Path) -> None:
    # Output is streamed directly to the terminal so that progress and errors are visible as they occur.
    result = subprocess.run(command, cwd=cwd, check=False)

    if result.returncode != 0:
        typer.secho(
            f"\nERROR: '{subprocess.list2cmdline(map(str, command))}' failed with exit code {result.returncode}.",
            fg=typer.colors.RED,
            err=True,
        )

        raise typer.Exit(result.returncode)


# ----------------------------------------------------------------------
def dotter(*args: str | Path) -> None:
    run(["uvx", "dbrownell_Dotter", *args], REPO_ROOT)


# ----------------------------------------------------------------------
def robotter(*args: str | Path) -> None:
    run(["uvx", "robotter", *args], ROBOTTER_DIR)


# ----------------------------------------------------------------------
@app.command()
def main(
    tools_dir: Annotated[
        Path,
        typer.Argument(
            file_okay=False,
            resolve_path=True,
            help="The directory where tools are stored.",
        ),
    ],
    force: Annotated[
        bool,
        typer.Option(
            "--force",
            help="Overwrite existing files.",
        ),
    ] = False,
    force_symbolic_links: Annotated[
        bool,
        typer.Option(
            "--force-symbolic-links",
            help="Force symbolic links even when source and destination are on different drives.",
        ),
    ] = False,
) -> None:
    """Installs the dotfiles on the current machine."""

    # Run dbrownell_Dotter
    dotter_config_filenames: list[str | Path] = [Path("Generic") / "generic.yaml"]

    if sys.platform == "win32":
        dotter_config_filenames.append(Path("Windows") / "windows.yaml")

    dotter_args: list[str | Path] = [
        "Install",
        *dotter_config_filenames,
        "--var",
        f"tools_dir={tools_dir}",
    ]

    if force:
        dotter_args.append("--force")

    if force_symbolic_links:
        dotter_args.append("--force-symbolic-links")

    dotter(*dotter_args)

    # Run robotter
    for skill_dir in sorted((ROBOTTER_DIR / "skills").iterdir()):
        if skill_dir.is_dir():
            robotter("render_skill", f"skills/{skill_dir.name}", "claude-code")


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app()
