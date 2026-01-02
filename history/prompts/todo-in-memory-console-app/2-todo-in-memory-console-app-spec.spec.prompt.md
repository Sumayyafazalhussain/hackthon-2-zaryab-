---
id: 2
title: Todo In-Memory Console App Spec
stage: spec
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-in-memory-console-app
branch: 001-todo-in-memory-cli
user: Siddiqui
command: /sp.specify
labels: [specification, todo, python, cli]
links:
  spec: specs/001-todo-in-memory-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/001-todo-in-memory-cli/spec.md
 - specs/001-todo-in-memory-cli/checklists/requirements.md
tests:
 - null
---

## Prompt

```
/sp.specify # Specification: Phase I – Todo In-Memory Console App ## Objective Build a Python console-based Todo application that manages tasks entirely in memory using a fully interactive, menu-driven CLI. The application MUST run continuously in a loop and terminate ONLY when the user explicitly selects the Exit option. --- ## Data Model (In-Memory) ### Task Each task MUST contain the following fields: - id: integer (auto-increment, unique) - title: string (required) - description: string (optional) - completed: boolean (default: false) - priority: string (Low | Medium | High) - category: string (default: "General") All tasks are stored in a Python list during runtime. No files or databases are allowed. --- ## Global CLI Rules - No command-line flags or arguments - All actions MUST be menu-driven - Application MUST run inside an infinite loop - Menu MUST reappear after every operation - Program exits ONLY when user selects Exit - Invalid input MUST NOT crash the application --- ## Main Menu (Required) 1. Add Task 2. View All Tasks 3. Update Task 4. Delete Task 5. Mark Task Complete / Incomplete 6. Filter Tasks 7. Exit --- ## Features & Acceptance Criteria --- ### 1. Add Task **User Story** As a user, I want to add a task so I can remember what to do. **Rules** - Title is REQUIRED - Description is OPTIONAL - Priority is REQUIRED (Low / Medium / High) - Category is OPTIONAL (default: "General") - ID is generated automatically - Task is stored in memory **CLI Behavior** - Prompt for title - Prompt for description - Prompt for priority (validate input) - Prompt for category - Confirm successful creation with task ID --- ### 2. View All Tasks **User Story** As a user, I want to see all my tasks. **Rules** - Display all tasks - Show ID, title, priority, category, and status - Completed tasks MUST be clearly marked **Example Output** [ ] 1 - Buy groceries | Medium | Personal [x] 2 - Call mom | Low | Family --- ### 3. Update Task **User Story** As a user, I want to update an existing task. **Rules** - User selects task by ID - User can update: - title - description - priority - category - Empty input keeps the previous value - If ID not found, show a clear error message --- ### 4. Delete Task **User Story** As a user, I want to delete a task I no longer need. **Rules** - User selects task by ID - Task is removed from memory - Confirm deletion - If ID not found, show error --- ### 5. Mark Task Complete / Incomplete **User Story** As a user, I want to mark a task as done or undone. **Rules** - User selects task by ID - Completion status is toggled - Updated status is displayed - If ID not found, show error --- ### 6. Filter Tasks #### 6.1 Filter by Category **Rules** - Prompt user for category name - Case-insensitive exact match - Display only matching tasks - If no tasks found, show friendly message #### 6.2 Filter by Priority **Rules** - Prompt user to choose priority (Low / Medium / High) - Display only matching tasks - Filtering MUST NOT modify tasks --- ## Error Handling - Invalid menu choice shows an error and re-displays menu - Invalid task ID shows a clear error message - Invalid priority input re-prompts the user --- ## Exit Behavior - Exit option terminates the loop gracefully - Display a goodbye message --- ## Non-Goals (Strictly Forbidden) - File persistence - Databases - Authentication - Web or GUI interfaces - Advanced tagging systems - Date or time-based sorting This specification is FINAL for Phase I.
```

## Response snapshot

Created comprehensive feature specification for the Todo In-Memory Console App with:
- 7 prioritized user stories covering all required functionality
- Detailed acceptance scenarios for each user story
- Complete functional requirements aligned with the constitution
- Success criteria with measurable outcomes
- Edge cases identified and addressed
- Quality checklist created and validated

## Outcome

- ✅ Impact: Complete feature specification created with all required sections
- 🧪 Tests: No tests required for specification creation
- 📁 Files: Created spec.md and requirements.md checklist in specs/001-todo-in-memory-cli/
- 🔁 Next prompts: /sp.plan to create implementation plan
- 🧠 Reflection: Specification covers all requirements from the constitution and provides clear direction for implementation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All checklist items passed
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Create implementation plan based on this specification