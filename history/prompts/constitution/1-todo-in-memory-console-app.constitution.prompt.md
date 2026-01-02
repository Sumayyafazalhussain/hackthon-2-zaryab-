---
id: 1
title: Todo In-Memory Console App Constitution
stage: constitution
date: 2026-01-02
surface: agent
model: Qwen
feature: todo-in-memory-console-app
branch: main
user: Siddiqui
command: /sp.constitution
labels: [constitution, todo, python, cli]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - null
---

## Prompt

```
/sp.constitution # Phase I – Todo In-Memory Console App  
(Spec-Driven Development)

---

## Constitution

### Core Principle
This project MUST follow Spec-Driven Development using Spec-Kit Plus and Claude Code.  
No source code will be written manually by the developer.

### Scope Lock
This constitution applies ONLY to:
- Phase I: In-Memory Python Console Application

The following are STRICTLY OUT OF SCOPE:
- Web
- Database
- Authentication
- AI / Chatbot
- Kubernetes
- Cloud

### Technology Constraints
- Python 3.13+
- Console-based application only
- In-memory storage (no files, no database)
- Standard Python libraries only

### Development Rules
1. All features MUST originate from specs.
2. Claude Code is the ONLY entity allowed to write or modify code.
3. Developer may ONLY:
   - Refine specifications
   - Review generated code
   - Run the application
4. Clean architecture and readable structure are mandatory.
5. Each task MUST have a unique ID generated in memory.

### Functional Boundaries
The application MUST support ONLY:
- Add Task
- View Tasks
- Update Task
- Delete Task
- Mark Task as Complete / Incomplete
- Assign Priority
- Assign Category
- Filter Tasks by Priority or Category

❌ No databases  
❌ No file saving  
❌ No authentication  
❌ No advanced tagging systems  
❌ No date-based sorting  

### CLI Enforcement
- No command-line flags or arguments
- Fully menu-driven interaction
- Application MUST run in an infinite loop
- Program exits ONLY when user selects "Exit"
```

## Response snapshot

Constitution file created with the following principles:
- Spec-Driven Development using Spec-Kit Plus and Claude Code
- Scope limited to In-Memory Python Console Application
- Technology constraints: Python 3.13+, console-based, in-memory storage
- Development rules: Claude Code writes all source code
- Functional boundaries: Add/View/Update/Delete tasks with priority/category filtering
- CLI enforcement: menu-driven, no flags/args

Templates updated to align with constitution:
- Plan template: Added constitution compliance verification
- Spec template: Added functional requirements aligned with constitution
- Tasks template: Added constitution-compliant tasks

## Outcome

- ✅ Impact: Created constitution file and updated templates to align with project principles
- 🧪 Tests: No tests required for constitution update
- 📁 Files: Updated 4 files (.specify/memory/constitution.md, .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md)
- 🔁 Next prompts: /sp.specify to implement the feature specification
- 🧠 Reflection: Constitution provides clear boundaries and constraints for the project

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Implement the feature specification based on the constitution