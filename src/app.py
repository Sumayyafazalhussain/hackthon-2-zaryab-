"""
Main application logic for the Todo In-Memory Console App.

This module contains the main application loop and routing logic.
"""

from src.task_manager import TaskManager
from src.menu import (
    display_main_menu, display_filter_menu, get_user_choice,
    get_task_details, get_task_id, get_task_updates,
    get_filter_category, get_filter_priority
)


class TodoApp:
    """
    Main application class that handles the CLI loop and user interactions.
    """
    
    def __init__(self):
        """
        Initialize the application with a task manager.
        """
        self.task_manager = TaskManager()
        self.running = True

    def run(self):
        """
        Start the main application loop.
        """
        print("Welcome to the Todo In-Memory Console App!")
        print("All data is stored in memory only and will be lost when the application exits.")
        
        while self.running:
            display_main_menu()
            choice = get_user_choice()
            
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_all_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_completion()
            elif choice == "6":
                self.filter_tasks()
            elif choice == "7":
                self.exit_app()
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
    
    def add_task(self):
        """
        Handle the add task functionality.
        """
        try:
            title, description, priority, category = get_task_details()
            
            # Validate required fields
            if not title:
                print("Title is required. Task not added.")
                return
            
            task = self.task_manager.add_task(title, description, priority, category)
            print(f"Task added successfully with ID: {task.id}")
        except ValueError as e:
            print(f"Error adding task: {e}")
        except Exception as e:
            print(f"Unexpected error adding task: {e}")
    
    def view_all_tasks(self):
        """
        Handle the view all tasks functionality.
        """
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            print("\nNo tasks found.")
            return
        
        print("\nAll Tasks:")
        for task in tasks:
            print(task)
    
    def update_task(self):
        """
        Handle the update task functionality.
        """
        task_id = get_task_id("Enter the ID of the task to update: ")
        if task_id is None:
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        
        updates = get_task_updates()
        
        if not updates:
            print("No updates provided. Task not modified.")
            return
        
        success = self.task_manager.update_task(
            task_id, 
            title=updates.get('title'),
            description=updates.get('description'),
            priority=updates.get('priority'),
            category=updates.get('category')
        )
        
        if success:
            print(f"Task with ID {task_id} updated successfully.")
        else:
            print(f"Failed to update task with ID {task_id}.")
    
    def delete_task(self):
        """
        Handle the delete task functionality.
        """
        task_id = get_task_id("Enter the ID of the task to delete: ")
        if task_id is None:
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        
        success = self.task_manager.delete_task(task_id)
        
        if success:
            print(f"Task with ID {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task with ID {task_id}.")
    
    def toggle_task_completion(self):
        """
        Handle the toggle task completion functionality.
        """
        task_id = get_task_id("Enter the ID of the task to toggle: ")
        if task_id is None:
            return
        
        task = self.task_manager.get_task_by_id(task_id)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return
        
        success = self.task_manager.toggle_task_completion(task_id)
        
        if success:
            status = "completed" if task.completed else "incomplete"
            print(f"Task with ID {task_id} marked as {status}.")
        else:
            print(f"Failed to toggle completion status for task with ID {task_id}.")
    
    def filter_tasks(self):
        """
        Handle the filter tasks functionality.
        """
        while True:
            display_filter_menu()
            choice = get_user_choice()
            
            if choice == "1":
                self.filter_by_category()
                break
            elif choice == "2":
                self.filter_by_priority()
                break
            elif choice == "3":
                break  # Go back to main menu
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
    
    def filter_by_category(self):
        """
        Handle filtering tasks by category.
        """
        category = get_filter_category()
        
        if not category:
            print("Category cannot be empty.")
            return
        
        tasks = self.task_manager.filter_tasks_by_category(category)
        
        if not tasks:
            print(f"No tasks found with category '{category}'.")
            return
        
        print(f"\nTasks with category '{category}':")
        for task in tasks:
            print(task)
    
    def filter_by_priority(self):
        """
        Handle filtering tasks by priority.
        """
        priority = get_filter_priority()
        
        tasks = self.task_manager.filter_tasks_by_priority(priority)
        
        if not tasks:
            print(f"No tasks found with priority '{priority}'.")
            return
        
        print(f"\nTasks with priority '{priority}':")
        for task in tasks:
            print(task)
    
    def exit_app(self):
        """
        Handle the exit functionality.
        """
        print("Goodbye! All data was stored in memory only and has been lost.")
        self.running = False