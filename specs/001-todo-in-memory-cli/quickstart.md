# Quickstart Guide: Todo In-Memory Console App

## Prerequisites
- Python 3.13 or higher
- No additional dependencies required

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