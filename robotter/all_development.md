# File Format
Adhere to these principles when writing files.

- Line endings for new content should match the line endings in the rest of the file. When creating a new file, match the convention for the other files in the repository.

# Architectural Principles
Adhere to these architectural principles when planning and writing code.

- Don't Repeat Yourself (DRY)
- SOLID
- Generate the least amount of code possible
- Never modify code associated with the system under test when writing tests.

# Documentation
Adhere to these principles when generating code comments or documentation.

- Do not introduce documentation for code that is common or easily understood.
- Explain why code was introduced, not what the code is doing.
- Generate short, crisp documentation rather than verbose prose.

# Static Analysis/Linting Errors
Do not suppress static analysis/linting-style errors; attempt to address the problem instead. Consult the human if the problem cannot be properly addressed.