<!-- Version: 0.3.0 -->

{{ include_configuration("all_development.md") }}

# Python Development
Adhere to these conventions when writing python code.

## Naming
Use these conventions when writing python code:

- Class names use `PascalCase`.
- Function and method names use `PascalCase`.
- Variables use `snake_case`.
- Filenames use `snake_case` (but this is not required).

## Type Annotations
Adhere to these conventions when adding type annotations to python code.

- Do not use `Any` in production code; use `object` instead.

## Testing
Use these conventions when writing or exercising tests:

- Run tests on the command line via `uv run pytest`; do not attempt to change the directory before running the tests.
- Never write tests for private functionality or class members (these are entities whose name begins with `_`).
- All tests must assert functionality.
- Never remove code to make tests pass.
- Compare entire strings when asserting that strings are equal.
- Use `textwrap.dedent` to compare strings with multiple lines.

## Imports
Order imports according to this example:

1. Python library module imports (if any).
2. Python library from imports (if any).
3. 3rd party module imports (if any).
4. 3rd party from imports (if any).
5. Package imports (if any).

Separate each section with a blank line.

```python
import os
import sys

from pathlib import Path

import typer

from dbrownell_Common.Streams.DoneManager import DoneManager
from dbrownell_Common import TextwrapEx

from MyPackage import my_functionality
```

## Documentation
Use these conventions when generating code comments or documentation.

- Generate short docstrings.
