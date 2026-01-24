"""
Unit tests for the Todo In-Memory Console App.
"""
import unittest
import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from task_model import Task
from task_manager import TaskManager


class TestTask(unittest.TestCase):
    """Test the Task class."""
    
    def test_task_creation_valid(self):
        """Test creating a valid task."""
        task = Task(1, "Test Task", "Test Description", False, "High", "Work")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.category, "Work")
    
    def test_task_creation_defaults(self):
        """Test creating a task with default values."""
        task = Task(1, "Test Task")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "")
        self.assertEqual(task.completed, False)
        self.assertEqual(task.priority, "Medium")  # Default priority
        self.assertEqual(task.category, "General")  # Default category
    
    def test_task_creation_invalid_id(self):
        """Test creating a task with invalid ID."""
        with self.assertRaises(ValueError):
            Task(0, "Test Task")  # ID must be positive
        
        with self.assertRaises(ValueError):
            Task(-1, "Test Task")  # ID must be positive
    
    def test_task_creation_invalid_title(self):
        """Test creating a task with invalid title."""
        with self.assertRaises(ValueError):
            Task(1, "")  # Title cannot be empty
        
        with self.assertRaises(ValueError):
            Task(1, "   ")  # Title cannot be just whitespace
    
    def test_task_creation_invalid_priority(self):
        """Test creating a task with invalid priority."""
        with self.assertRaises(ValueError):
            Task(1, "Test Task", "Description", False, "Invalid", "Work")
    
    def test_task_creation_invalid_completed(self):
        """Test creating a task with invalid completed status."""
        with self.assertRaises(ValueError):
            Task(1, "Test Task", "Description", "invalid", "High", "Work")  # Should be boolean
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(1, "Test Task", "Test Description", True, "Low", "Personal")
        task_dict = task.to_dict()
        
        expected = {
            "id": 1,
            "title": "Test Task",
            "description": "Test Description",
            "completed": True,
            "priority": "Low",
            "category": "Personal"
        }
        
        self.assertEqual(task_dict, expected)
    
    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task_completed = Task(1, "Test Task", "Description", True, "High", "Work")
        self.assertEqual(str(task_completed), "[x] 1 - Test Task | High | Work")
        
        task_incomplete = Task(2, "Test Task", "Description", False, "Low", "Personal")
        self.assertEqual(str(task_incomplete), "[ ] 2 - Test Task | Low | Personal")


class TestTaskManager(unittest.TestCase):
    """Test the TaskManager class."""
    
    def setUp(self):
        """Set up a fresh TaskManager for each test."""
        self.tm = TaskManager()
    
    def test_initial_state(self):
        """Test the initial state of TaskManager."""
        self.assertEqual(len(self.tm.get_all_tasks()), 0)
        self.assertEqual(self.tm.next_id, 1)
    
    def test_add_task(self):
        """Test adding a task."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        self.assertEqual(task.id, 1)
        self.assertEqual(len(self.tm.get_all_tasks()), 1)
        self.assertEqual(self.tm.next_id, 2)
        
        retrieved_task = self.tm.get_task_by_id(1)
        self.assertIsNotNone(retrieved_task)
        self.assertEqual(retrieved_task.title, "Test Task")
    
    def test_get_task_by_id(self):
        """Test getting a task by ID."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        found_task = self.tm.get_task_by_id(1)
        self.assertEqual(found_task, task)
        
        not_found_task = self.tm.get_task_by_id(999)
        self.assertIsNone(not_found_task)
    
    def test_update_task(self):
        """Test updating a task."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        # Update the task
        success = self.tm.update_task(1, title="Updated Task", priority="Low")
        self.assertTrue(success)
        
        updated_task = self.tm.get_task_by_id(1)
        self.assertEqual(updated_task.title, "Updated Task")
        self.assertEqual(updated_task.priority, "Low")
        self.assertEqual(updated_task.description, "Description")  # Should remain unchanged
        self.assertEqual(updated_task.category, "Work")  # Should remain unchanged
    
    def test_update_task_not_found(self):
        """Test updating a non-existent task."""
        success = self.tm.update_task(999, title="Updated Task")
        self.assertFalse(success)
    
    def test_update_task_empty_values(self):
        """Test updating a task with empty values (should preserve existing values)."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        # Update with empty strings for title and priority (should not update)
        success = self.tm.update_task(1, title="", priority="")
        self.assertTrue(success)
        
        # Values should remain unchanged
        updated_task = self.tm.get_task_by_id(1)
        self.assertEqual(updated_task.title, "Test Task")
        self.assertEqual(updated_task.priority, "High")
    
    def test_delete_task(self):
        """Test deleting a task."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        success = self.tm.delete_task(1)
        self.assertTrue(success)
        self.assertEqual(len(self.tm.get_all_tasks()), 0)
        self.assertIsNone(self.tm.get_task_by_id(1))
    
    def test_delete_task_not_found(self):
        """Test deleting a non-existent task."""
        success = self.tm.delete_task(999)
        self.assertFalse(success)
    
    def test_toggle_task_completion(self):
        """Test toggling task completion."""
        task = self.tm.add_task("Test Task", "Description", "High", "Work")
        
        # Initially should be incomplete
        self.assertFalse(task.completed)
        
        # Toggle to complete
        success = self.tm.toggle_task_completion(1)
        self.assertTrue(success)
        
        toggled_task = self.tm.get_task_by_id(1)
        self.assertTrue(toggled_task.completed)
        
        # Toggle back to incomplete
        success = self.tm.toggle_task_completion(1)
        self.assertTrue(success)
        
        toggled_task = self.tm.get_task_by_id(1)
        self.assertFalse(toggled_task.completed)
    
    def test_toggle_task_completion_not_found(self):
        """Test toggling completion of a non-existent task."""
        success = self.tm.toggle_task_completion(999)
        self.assertFalse(success)
    
    def test_filter_tasks_by_category(self):
        """Test filtering tasks by category."""
        self.tm.add_task("Task 1", "Description", "High", "Work")
        self.tm.add_task("Task 2", "Description", "Low", "Personal")
        self.tm.add_task("Task 3", "Description", "Medium", "Work")
        
        work_tasks = self.tm.filter_tasks_by_category("Work")
        self.assertEqual(len(work_tasks), 2)
        
        personal_tasks = self.tm.filter_tasks_by_category("Personal")
        self.assertEqual(len(personal_tasks), 1)
        
        # Test case-insensitive matching
        work_tasks_case = self.tm.filter_tasks_by_category("work")
        self.assertEqual(len(work_tasks_case), 2)
    
    def test_filter_tasks_by_priority(self):
        """Test filtering tasks by priority."""
        self.tm.add_task("Task 1", "Description", "High", "Work")
        self.tm.add_task("Task 2", "Description", "Low", "Personal")
        self.tm.add_task("Task 3", "Description", "High", "Personal")
        
        high_tasks = self.tm.filter_tasks_by_priority("High")
        self.assertEqual(len(high_tasks), 2)
        
        low_tasks = self.tm.filter_tasks_by_priority("Low")
        self.assertEqual(len(low_tasks), 1)
        
        # Test case-insensitive matching
        high_tasks_case = self.tm.filter_tasks_by_priority("high")
        self.assertEqual(len(high_tasks_case), 2)


if __name__ == '__main__':
    unittest.main()
    # test
