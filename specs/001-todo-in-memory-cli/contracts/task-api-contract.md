# API Contracts: Todo In-Memory Console App

## Task Management Endpoints

### Add Task
- **Operation**: Create a new task
- **Input**: title (required), description (optional), priority (required), category (optional)
- **Output**: Task object with assigned ID
- **Validation**: 
  - Title must not be empty
  - Priority must be one of: Low, Medium, High
- **Error Handling**: Return error message if validation fails

### View All Tasks
- **Operation**: Retrieve all tasks
- **Input**: None
- **Output**: List of all tasks with their details
- **Validation**: None
- **Error Handling**: None

### Update Task
- **Operation**: Update an existing task
- **Input**: task ID (required), new values for fields
- **Output**: Updated task object
- **Validation**: 
  - Task ID must exist
  - Priority must be one of: Low, Medium, High (if provided)
- **Error Handling**: Return error if task ID doesn't exist

### Delete Task
- **Operation**: Remove a task
- **Input**: task ID (required)
- **Output**: Confirmation message
- **Validation**: Task ID must exist
- **Error Handling**: Return error if task ID doesn't exist

### Mark Task Complete/Incomplete
- **Operation**: Toggle task completion status
- **Input**: task ID (required)
- **Output**: Updated task with toggled completion status
- **Validation**: Task ID must exist
- **Error Handling**: Return error if task ID doesn't exist

### Filter Tasks by Category
- **Operation**: Filter tasks by category
- **Input**: category name (required)
- **Output**: List of tasks matching the category
- **Validation**: None
- **Error Handling**: Return empty list if no matches

### Filter Tasks by Priority
- **Operation**: Filter tasks by priority
- **Input**: priority (required)
- **Output**: List of tasks matching the priority
- **Validation**: Priority must be one of: Low, Medium, High
- **Error Handling**: Return error if priority is invalid