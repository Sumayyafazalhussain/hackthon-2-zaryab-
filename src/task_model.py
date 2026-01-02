"""
Task model for the Todo In-Memory Console App.

This module defines the Task class with validation rules as specified in the data model.
"""

class Task:
    """
    Represents a single todo item with id, title, description, completed, priority, and category.
    """
    
    def __init__(self, task_id, title, description="", completed=False, priority="Medium", category="General"):
        """
        Initialize a Task instance.
        
        Args:
            task_id (int): Unique identifier for the task (auto-increment)
            title (str): Task title (required)
            description (str): Task description (optional, defaults to empty string)
            completed (bool): Completion status (defaults to False)
            priority (str): Task priority (Low, Medium, or High; defaults to Medium)
            category (str): Task category (defaults to "General")
        
        Raises:
            ValueError: If validation rules are violated
        """
        self.id = self._validate_id(task_id)
        self.title = self._validate_title(title)
        self.description = description
        self.completed = self._validate_completed(completed)
        self.priority = self._validate_priority(priority)
        self.category = self._validate_category(category)

    def _validate_id(self, task_id):
        """Validate the task ID."""
        if not isinstance(task_id, int) or task_id <= 0:
            raise ValueError("Task ID must be a positive integer")
        return task_id

    def _validate_title(self, title):
        """Validate the task title."""
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title must be a non-empty string")
        return title.strip()

    def _validate_completed(self, completed):
        """Validate the completed status."""
        if not isinstance(completed, bool):
            raise ValueError("Completed status must be a boolean value")
        return completed

    def _validate_priority(self, priority):
        """Validate the task priority."""
        valid_priorities = ["Low", "Medium", "High"]
        if priority not in valid_priorities:
            raise ValueError(f"Priority must be one of: {', '.join(valid_priorities)}")
        return priority

    def _validate_category(self, category):
        """Validate the task category."""
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        return category.strip() if category.strip() else "General"

    def to_dict(self):
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "priority": self.priority,
            "category": self.category
        }

    def __str__(self):
        """String representation of the task."""
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.id} - {self.title} | {self.priority} | {self.category}"