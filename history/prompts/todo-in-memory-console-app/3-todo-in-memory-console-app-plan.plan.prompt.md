---
id: 3
title: Todo In-Memory Console App Plan
stage: plan
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-in-memory-console-app
branch: 001-todo-in-memory-cli
user: Siddiqui
command: /sp.plan
labels: [planning, todo, python, cli]
links:
  spec: specs/001-todo-in-memory-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-todo-in-memory-cli/plan.md
 - specs/001-todo-in-memory-cli/research.md
 - specs/001-todo-in-memory-cli/data-model.md
 - specs/001-todo-in-memory-cli/quickstart.md
 - specs/001-todo-in-memory-cli/contracts/task-api-contract.md
tests:
 - null
---

## Prompt

```
/sp.plan 
Phase I – Todo In-Memory Console App

---

## Purpose
This plan defines the step-by-step execution strategy for building the Phase I Todo Console Application using Spec-Driven Development.

Claude Code MUST follow this plan strictly.  
No manual coding by the developer is allowed.

---

## Phase Scope
- Console-based Python application
- In-memory task management only
- Menu-driven CLI
- Infinite loop until user exits

---

## Project Structure (Mandatory)

The project MUST follow this structure:
project-root/
│
├── src/
│ ├── task_manager.py # create, update, delete, filter tasks
│ ├── task_model.py # task data structure
│ ├── menu.py # menu display & user input
│ └── app.py # application loop & routing
│
└── main.py # entry point (calls src/app.py)


### Structure Rules
- ALL business logic MUST live inside the `src/` folder
- Task creation, update, deletion, completion, and filtering MUST be implemented inside `src/`
- `main.py` MUST ONLY start the application
- No logic is allowed outside `src/`

---

## Implementation Plan

### Step 1: Initialize Application State
- Inside `src/task_manager.py`:
  - Create an empty in-memory list to store tasks
  - Initialize an auto-incrementing task ID counter
- Prepare application entry point via `main.py`

---

### Step 2: Display Main Menu
- Inside `src/menu.py`
- Print a clear, numbered menu with options:
  1. Add Task
  2. View All Tasks
  3. Update Task
  4. Delete Task
  5. Mark Task Complete / Incomplete
  6. Filter Tasks
  7. Exit

---

### Step 3: Input Handling Loop
- Implemented in `src/app.py`
- Start an infinite loop
- Prompt user for menu selection
- Validate numeric input
- Route execution to appropriate functions in `task_manager.py`
- After completion, return to the main menu

---

### Step 4: Add Task Flow
- Implemented in `src/task_manager.py`
- Prompt user for:
  - Title (required)
  - Description (optional)
  - Priority (Low / Medium / High)
  - Category (default: General)
- Validate required fields
- Create task object using `task_model.py`
- Append task to in-memory list
- Display success confirmation

---

### Step 5: View All Tasks Flow
- Implemented in `src/task_manager.py`
- Check if task list is empty
- Iterate over task list
- Display each task with:
  - Completion indicator
  - ID
  - Title
  - Priority
  - Category

---

### Step 6: Update Task Flow
- Implemented in `src/task_manager.py`
- Prompt user for task ID
- Locate task in memory
- If not found, display error
- Prompt for new values:
  - Title
  - Description
  - Priority
  - Category
- Preserve existing values if input is empty
- Confirm successful update

---

### Step 7: Delete Task Flow
- Implemented in `src/task_manager.py`
- Prompt user for task ID
- Locate task
- If not found, display error
- Remove task from list
- Confirm deletion

---

### Step 8: Mark Task Complete / Incomplete Flow
- Implemented in `src/task_manager.py`
- Prompt user for task ID
- Locate task
- Toggle completed status
- Display updated state

---

### Step 9: Filter Tasks Menu
- Implemented in `src/menu.py`
- Display filter sub-menu:
  1. Filter by Category
  2. Filter by Priority
  3. Back to Main Menu

---

### Step 10: Filter by Category
- Implemented in `src/task_manager.py`
- Prompt for category name
- Perform case-insensitive exact match
- Display matching tasks
- If none found, display friendly message

---

### Step 11: Filter by Priority
- Implemented in `src/task_manager.py`
- Prompt for priority (Low / Medium / High)
- Validate input
- Display matching tasks
- If none found, display friendly message

---

### Step 12: Error Handling Strategy
- Centralized input validation
- Prevent crashes on invalid input
- Display user-friendly error messages
- Re-prompt user when necessary

---

### Step 13: Exit Flow
- Implemented in `src/app.py`
- Detect Exit option selection
- Display goodbye message
- Terminate application gracefully

---

## Constraints Enforcement
- No command-line flags or arguments
- No file system usage
- No database usage
- No external libraries
- No advanced features beyond specification

---

## Completion Criteria
The application is considered complete when:
- All menu options function correctly
- Infinite loop operates until Exit
- All task operations occur inside `src/`
- `main.py` only starts the application
- All features match `/sp.specify.md`
- No out-of-scope functionality exists

---

This plan is FINAL for Phase I.
```

## Response snapshot

Created comprehensive implementation plan for the Todo In-Memory Console App with:
- Filled technical context with Python 3.13+, standard libraries, in-memory storage
- Updated project structure to match required format
- Created research.md resolving all clarifications
- Created data-model.md defining the Task entity
- Created quickstart.md guide for users
- Created API contracts for task management operations
- Verified all constitution compliance requirements
- Updated agent context with project details

## Outcome

- ✅ Impact: Complete implementation plan with all required artifacts
- 🧪 Tests: No tests required for planning phase
- 📁 Files: Created plan.md, research.md, data-model.md, quickstart.md, and contracts/
- 🔁 Next prompts: /sp.tasks to break the plan into tasks
- 🧠 Reflection: Plan aligns with constitution and specification, ready for task breakdown

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All constitution checks passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Break the plan into specific implementation tasks