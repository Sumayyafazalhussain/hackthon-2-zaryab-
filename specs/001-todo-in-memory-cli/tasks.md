---

description: "Task list for Todo In-Memory Console App implementation"
---

# Tasks: Todo In-Memory Console App

**Input**: Design documents from `/specs/001-todo-in-memory-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Initialize Python 3.13+ project with standard library dependencies only
- [ ] T003 [P] Configure linting and formatting tools
- [X] T004 Ensure no database or file persistence dependencies are added
- [X] T005 Set up in-memory storage mechanism (Python list for tasks)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 [P] Create base Task model with id, title, description, completed, priority, category in src/task_model.py
- [X] T007 [P] Implement in-memory task storage mechanism using Python list in src/task_manager.py
- [X] T008 Configure error handling and input validation infrastructure in src/app.py
- [X] T009 Setup CLI menu system structure without command-line arguments in src/menu.py
- [X] T010 Create task management service with add, view, update, delete, mark complete/incomplete functionality in src/task_manager.py
- [X] T011 Implement filtering functionality by priority and category in src/task_manager.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks with title, description, priority, and category

**Independent Test**: User can successfully add a new task with title, description, priority, and category, and see it listed in the task list.

### Implementation for User Story 1

- [X] T012 [P] [US1] Implement Task class with validation in src/task_model.py
- [X] T013 [US1] Implement add_task function in src/task_manager.py
- [X] T014 [US1] Create add_task menu interface in src/menu.py
- [X] T015 [US1] Integrate add_task functionality with main app loop in src/app.py
- [X] T016 [US1] Add validation for required fields (title, priority) in src/task_manager.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to see all their tasks with clear status indicators

**Independent Test**: User can view all tasks with their ID, title, priority, category, and completion status clearly displayed.

### Implementation for User Story 2

- [X] T017 [P] [US2] Implement view_all_tasks function in src/task_manager.py
- [X] T018 [US2] Create view_all_tasks menu interface in src/menu.py
- [X] T019 [US2] Integrate view_all_tasks functionality with main app loop in src/app.py
- [X] T020 [US2] Add clear visual indicators for completed/incomplete tasks in src/task_manager.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 7 - Exit Application (Priority: P1)

**Goal**: Enable users to exit the application cleanly

**Independent Test**: User can select "Exit" from the main menu and the application terminates gracefully with a goodbye message.

### Implementation for User Story 7

- [X] T021 [US7] Implement exit functionality in src/app.py
- [X] T022 [US7] Create exit menu option in src/menu.py
- [X] T023 [US7] Add goodbye message display on exit in src/app.py

**Checkpoint**: At this point, User Stories 1, 2, and 7 should all work independently

---

## Phase 6: User Story 3 - Mark Task Complete / Incomplete (Priority: P2)

**Goal**: Enable users to toggle task completion status

**Independent Test**: User can select a task by ID and toggle its completion status, with the change reflected in the task list.

### Implementation for User Story 3

- [X] T024 [US3] Implement toggle_task_completion function in src/task_manager.py
- [X] T025 [US3] Create toggle_task_completion menu interface in src/menu.py
- [X] T026 [US3] Integrate toggle_task_completion functionality with main app loop in src/app.py

**Checkpoint**: At this point, User Stories 1, 2, 3, and 7 should all work independently

---

## Phase 7: User Story 4 - Update Task (Priority: P2)

**Goal**: Enable users to update existing task details

**Independent Test**: User can select a task by ID and update its title, description, priority, or category.

### Implementation for User Story 4

- [X] T027 [US4] Implement update_task function in src/task_manager.py
- [X] T028 [US4] Create update_task menu interface in src/menu.py
- [X] T029 [US4] Integrate update_task functionality with main app loop in src/app.py
- [X] T030 [US4] Add functionality to preserve existing values when input is empty in src/task_manager.py

**Checkpoint**: At this point, User Stories 1, 2, 3, 4, and 7 should all work independently

---

## Phase 8: User Story 5 - Delete Task (Priority: P3)

**Goal**: Enable users to delete tasks they no longer need

**Independent Test**: User can select a task by ID and remove it from the in-memory list.

### Implementation for User Story 5

- [X] T031 [US5] Implement delete_task function in src/task_manager.py
- [X] T032 [US5] Create delete_task menu interface in src/menu.py
- [X] T033 [US5] Integrate delete_task functionality with main app loop in src/app.py

**Checkpoint**: At this point, User Stories 1, 2, 3, 4, 5, and 7 should all work independently

---

## Phase 9: User Story 6 - Filter Tasks (Priority: P3)

**Goal**: Enable users to filter tasks by category or priority

**Independent Test**: User can filter tasks by category or priority and see only matching tasks.

### Implementation for User Story 6

- [X] T034 [P] [US6] Implement filter_by_category function in src/task_manager.py
- [X] T035 [P] [US6] Implement filter_by_priority function in src/task_manager.py
- [X] T036 [US6] Create filter_tasks menu interface in src/menu.py
- [X] T037 [US6] Integrate filter_tasks functionality with main app loop in src/app.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T038 [P] Documentation updates in docs/
- [ ] T039 Code cleanup and refactoring
- [ ] T040 Performance optimization across all stories
- [X] T041 [P] Additional unit tests in tests/
- [ ] T042 Security hardening
- [X] T043 Run quickstart.md validation
- [X] T044 Verify no database or file persistence code was added
- [X] T045 Confirm CLI is menu-driven with no command-line flags/args
- [X] T046 Validate all functionality works without authentication
- [X] T047 Ensure no web interfaces were implemented
- [X] T048 Confirm no advanced tagging systems were added
- [X] T049 Create main.py entry point that calls src/app.py
- [X] T050 Final integration testing of all features

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 7 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 6 (P3)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all implementation tasks for User Story 1 together:
Task: "Implement Task class with validation in src/task_model.py"
Task: "Implement add_task function in src/task_manager.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, and 7 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Task)
4. Complete Phase 4: User Story 2 (View All Tasks)
5. Complete Phase 5: User Story 7 (Exit Application)
6. **STOP and VALIDATE**: Test User Stories 1, 2, and 7 independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 7 → Test independently → Deploy/Demo
5. Add User Story 3 → Test independently → Deploy/Demo
6. Add User Story 4 → Test independently → Deploy/Demo
7. Add User Story 5 → Test independently → Deploy/Demo
8. Add User Story 6 → Test independently → Deploy/Demo
9. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 7
   - Developer D: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence