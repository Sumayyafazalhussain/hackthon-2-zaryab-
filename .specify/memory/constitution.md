<!--
Sync Impact Report:
Version change: 1.0.0 -> 2.0.0
List of modified principles:
  - I. Clear Command-Line Interface (CLI) -> I. Console-Based CLI
  - II. Standard I/O -> II. Standard I/O (Remains)
  - III. Test-Driven Development (TDD) -> III. Test-Driven Development (TDD) (Remains)
  - IV. Graceful Error Handling -> IV. Graceful Error Handling (Remains)
  - V. Simplicity -> V. Clean, Readable, and Modular Code
  - New Principles: VI. Single Responsibility Principle, VII. Python Standard Library Only, VIII. Unique Task IDs, IX. Clear User Prompts and Outputs, X. Beginner-Friendly Code, XI. Small and Clear Functions, XII. Easy-to-Understand Output
Added sections: Non-Goals, Quality Bar
Removed sections: None
Templates requiring updates:
  - .specify/templates/plan-template.md: ✅ updated
  - .specify/templates/spec-template.md: ✅ updated
  - .specify/templates/tasks-template.md: ✅ updated
  - .specify/templates/commands/sp.adr.toml: ✅ updated
  - .specify/templates/commands/sp.analyze.toml: ✅ updated
  - .specify/templates/commands/sp.checklist.toml: ✅ updated
  - .specify/templates/commands/sp.clarify.toml: ✅ updated
  - .specify/templates/commands/sp.constitution.toml: ✅ updated
  - .specify/templates/commands/sp.git.commit_pr.toml: ✅ updated
  - .specify/templates/commands/sp.implement.toml: ✅ updated
  - .specify/templates/commands/sp.phr.toml: ✅ updated
  - .specify/templates/commands/sp.plan.toml: ✅ updated
  - .specify/templates/commands/sp.reverse-engineer.toml: ✅ updated
  - .specify/templates/commands/sp.specify.toml: ✅ updated
  - .specify/templates/commands/sp.tasks.toml: ✅ updated
  - .specify/templates/commands/sp.taskstoissues.toml: ✅ updated
Follow-up TODOs: None
-->
# Todo CLI App Constitution

## Purpose
Build a simple in-memory Todo application using Python CLI following Spec-Driven Development.

## Core Principles

### I. Console-Based CLI
The application must run in the terminal (console-based). Every feature will be exposed through a clear and consistent command-line interface. Commands, arguments, and flags should be intuitive and well-documented.

### II. Standard I/O
The application will use standard input (stdin) for input and standard output (stdout) for output. Errors and logging information will be directed to standard error (stderr). This ensures compatibility with other command-line tools.

### III. Test-Driven Development (TDD)
All new features must be accompanied by tests. The Red-Green-Refactor cycle is to be followed to ensure code quality and maintainability.

### IV. Graceful Error Handling
The application must handle invalid input gracefully, providing clear and informative messages to the user. Exit codes should be used to indicate the success or failure of a command.

### V. Clean, Readable, and Modular Code
Code must be clean, readable, and modular, following the single-responsibility principle.

### VI. Single Responsibility Principle
Each component (function, class) should have one and only one reason to change.

### VII. Python Standard Library Only
No external libraries except Python standard library will be used.

### VIII. Unique Task IDs
Every task must have a unique ID.

### IX. Clear User Prompts and Outputs
Clear user prompts and outputs are required to ensure ease of use.

## Development Rules
- Do not add features outside the specification.

## Non-Goals
- No GUI
- No web framework
- No database
- No authentication

## Quality Bar
- Code must be beginner-friendly.
- Functions must be small and clear.
- Output must be easy to understand.

## Governance
This constitution is the supreme governing document of this project. Any changes to this constitution must be proposed as a pull request and approved by the project maintainers.

**Version**: 2.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
