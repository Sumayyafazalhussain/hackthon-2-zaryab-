<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: N/A (new constitution)
Added sections: Core Principles, Scope Lock, Technology Constraints, Development Rules, Functional Boundaries, CLI Enforcement
Removed sections: N/A
Templates requiring updates: 
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated  
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ✅ reviewed
- README.md ⚠ pending
Follow-up TODOs: None
-->

# Todo In-Memory Console App Constitution

## Core Principles

### I. Spec-Driven Development
This project MUST follow Spec-Driven Development using Spec-Kit Plus and Claude Code. No source code will be written manually by the developer.

### II. Scope Lock
This constitution applies ONLY to:
- Phase I: In-Memory Python Console Application

The following are STRICTLY OUT OF SCOPE:
- Web
- Database
- Authentication
- AI / Chatbot
- Kubernetes
- Cloud

### III. Technology Constraints
- Python 3.13+
- Console-based application only
- In-memory storage (no files, no database)
- Standard Python libraries only

### IV. Development Rules
1. All features MUST originate from specs.
2. Claude Code is the ONLY entity allowed to write or modify code.
3. Developer may ONLY:
   - Refine specifications
   - Review generated code
   - Run the application
4. Clean architecture and readable structure are mandatory.
5. Each task MUST have a unique ID generated in memory.

### V. Functional Boundaries
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

### VI. CLI Enforcement
- No command-line flags or arguments
- Fully menu-driven interaction
- Application MUST run in an infinite loop
- Program exits ONLY when user selects "Exit"

## Data Model Constraints
- Task ID: integer (auto-increment, unique)
- Task Title: string (required)
- Task Description: string (optional)
- Task Completed: boolean (default: false)
- Task Priority: string (Low | Medium | High)
- Task Category: string (default: "General")
- All tasks stored in a Python list during runtime only

## Global CLI Rules
- No flags or arguments
- Menu MUST reappear after every action
- User MUST explicitly choose Exit to terminate
- Invalid input must NOT crash the application

## Error Handling Requirements
- Invalid menu choice shows error and re-displays menu
- Invalid task ID shows clear message
- Invalid priority input re-prompts user

## Exit Behavior
- Exit option terminates loop gracefully
- Display goodbye message

## Non-Goals (Strictly Forbidden)
- File persistence
- Databases
- Authentication
- Web interfaces
- Advanced tagging
- Date/time sorting

## Governance
This constitution supersedes all other development practices. Amendments require documentation and approval. All pull requests and code reviews must verify compliance with these principles. The constitution version must be updated according to semantic versioning rules:
- MAJOR: Backward incompatible governance/principle removals or redefinitions
- MINOR: New principle/section added or materially expanded guidance
- PATCH: Clarifications, wording, typo fixes, non-semantic refinements

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02