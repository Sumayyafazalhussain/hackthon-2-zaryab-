"""
Task manager for the Todo In-Memory Console App.

This module handles all task-related operations including adding, viewing, updating,
deleting, and filtering tasks. All data is stored in memory only.
"""

from src.task_model import Task


class TaskManager:
    """
    Manages tasks in memory using a Python list.
    """
    
    def __init__(self):
        """
        Initialize the task manager with an empty task list and ID counter.
        """
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description="", priority="Medium", category="General"):
        """
        Add a new task to the in-memory list.
        
        Args:
            title (str): Task title (required)
            description (str): Task description (optional)
            priority (str): Task priority (Low, Medium, High; required)
            category (str): Task category (optional, defaults to "General")
        
        Returns:
            Task: The newly created task object
        """
        task = Task(
            task_id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            category=category
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        """
        Retrieve all tasks from memory.
        
        Returns:
            list: List of all Task objects
        """
        return self.tasks

    def get_task_by_id(self, task_id):
        """
        Find a task by its ID.
        
        Args:
            task_id (int): The ID of the task to find
        
        Returns:
            Task: The task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id, title=None, description=None, priority=None, category=None):
        """
        Update an existing task's details.

        Args:
            task_id (int): The ID of the task to update
            title (str, optional): New title (if provided)
            description (str, optional): New description (if provided)
            priority (str, optional): New priority (if provided)
            category (str, optional): New category (if provided)

        Returns:
            bool: True if task was updated, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        # Update fields if new values are provided and not empty, otherwise keep existing values
        if title is not None and title.strip():
            task.title = task._validate_title(title)
        if description is not None:
            task.description = description
        if priority is not None and priority.strip():
            task.priority = task._validate_priority(priority)
        if category is not None and category.strip():
            task.category = task._validate_category(category)

        return True

    def delete_task(self, task_id):
        """
        Remove a task from memory.
        
        Args:
            task_id (int): The ID of the task to delete
        
        Returns:
            bool: True if task was deleted, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        self.tasks.remove(task)
        return True

    def toggle_task_completion(self, task_id):
        """
        Toggle the completion status of a task.
        
        Args:
            task_id (int): The ID of the task to toggle
        
        Returns:
            bool: True if task status was toggled, False if task not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        task.completed = not task.completed
        return True

    def filter_tasks_by_category(self, category):
        """
        Filter tasks by category (case-insensitive exact match).
        
        Args:
            category (str): The category to filter by
        
        Returns:
            list: List of Task objects matching the category
        """
        category = category.strip().lower()
        return [task for task in self.tasks if task.category.lower() == category]

    def filter_tasks_by_priority(self, priority):
        """
        Filter tasks by priority.
        
        Args:
            priority (str): The priority to filter by (Low, Medium, High)
        
        Returns:
            list: List of Task objects matching the priority
        """
        return [task for task in self.tasks if task.priority.lower() == priority.lower()]