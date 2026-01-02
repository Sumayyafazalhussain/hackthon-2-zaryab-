# Todo In-Memory Console App

A Python console-based Todo application that manages tasks entirely in memory using a fully interactive, menu-driven CLI. The application runs continuously in a loop and terminates only when the user explicitly selects the Exit option.

## Features

- Add, view, update, and delete tasks
- Mark tasks as complete/incomplete
- Filter tasks by category or priority
- Menu-driven interface
- In-memory storage (no file/database persistence)
- Task properties: title, description, priority (Low/Medium/High), category

## Requirements

- Python 3.13 or higher

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is installed and available in your PATH

## Running the Application

1. Execute the main script: `python main.py`
2. The application will start and display the main menu
3. Follow the on-screen prompts to interact with the application

## Basic Usage

1. **Add Task**: Select option 1 to add a new task
   - Enter the task title (required)
   - Enter the task description (optional)
   - Enter the priority (Low/Medium/High)
   - Enter the category (optional, defaults to "General")

2. **View All Tasks**: Select option 2 to see all tasks
   - Completed tasks will be marked with [x]
   - Incomplete tasks will be marked with [ ]

3. **Update Task**: Select option 3 to update an existing task
   - Enter the task ID
   - Enter new values for each field (leave empty to keep existing value)

4. **Delete Task**: Select option 4 to remove a task
   - Enter the task ID to delete

5. **Mark Task Complete/Incomplete**: Select option 5 to toggle task completion
   - Enter the task ID to toggle its completion status

6. **Filter Tasks**: Select option 6 to filter tasks
   - Choose to filter by category or priority
   - Enter the filter criteria

7. **Exit**: Select option 7 to exit the application
   - The application will terminate gracefully

## Important Notes

- All data is stored in memory only and will be lost when the application exits
- Invalid inputs will be handled gracefully with error messages
- The application runs in an infinite loop until the user selects Exit

## Project Structure

```
project-root/
├── src/
│   ├── task_manager.py # create, update, delete, filter tasks
│   ├── task_model.py   # task data structure
│   ├── menu.py         # menu display & user input
│   └── app.py          # application loop & routing
├── main.py             # entry point (calls src/app.py)
├── tests/
│   ├── test_task_model.py
│   ├── test_task_manager.py
│   └── test_app.py
└── requirements.txt    # project dependencies (if any)
```

## Testing

To run the unit tests:

```bash
python -m pytest tests/ -v
```

## Architecture

This application follows a clean architecture with separation of concerns:

- `task_model.py`: Defines the Task entity with validation rules
- `task_manager.py`: Handles all task-related operations (CRUD and filtering)
- `menu.py`: Handles user interface and input collection
- `app.py`: Contains the main application loop and routing logic
- `main.py`: Entry point for the application