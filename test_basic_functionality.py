"""
Basic test to verify the Todo In-Memory Console App functionality.
"""

import sys
import os

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task_model import Task
from task_manager import TaskManager


def test_task_creation():
    """Test that tasks can be created with proper validation."""
    print("Testing task creation...")

    # Test valid task creation
    try:
        task = Task(1, "Test Task", "Test Description", False, "High", "Work")
        print(f"SUCCESS: Task created: {task}")
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.completed == False
        assert task.priority == "High"
        assert task.category == "Work"
        print("SUCCESS: Task attributes validated")
    except Exception as e:
        print(f"ERROR: Error creating valid task: {e}")
        return False

    # Test validation - empty title should raise error
    try:
        invalid_task = Task(2, "", "Empty title", False, "High", "Work")
        print("ERROR: Empty title should have raised an error")
        return False
    except ValueError:
        print("SUCCESS: Empty title correctly rejected")

    # Test validation - invalid priority should raise error
    try:
        invalid_task = Task(3, "Test Task", "Test Description", False, "Invalid", "Work")
        print("ERROR: Invalid priority should have raised an error")
        return False
    except ValueError:
        print("SUCCESS: Invalid priority correctly rejected")

    return True


def test_task_manager():
    """Test that the task manager works correctly."""
    print("\nTesting task manager...")

    tm = TaskManager()

    # Test adding a task
    task = tm.add_task("Test Task", "Test Description", "High", "Work")
    print(f"SUCCESS: Task added: {task}")
    assert len(tm.get_all_tasks()) == 1
    assert task.id == 1  # First task should have ID 1

    # Test getting all tasks
    all_tasks = tm.get_all_tasks()
    assert len(all_tasks) == 1
    print("SUCCESS: Task retrieval works")

    # Test getting task by ID
    found_task = tm.get_task_by_id(1)
    assert found_task is not None
    assert found_task.title == "Test Task"
    print("SUCCESS: Task lookup by ID works")

    # Test updating a task
    success = tm.update_task(1, title="Updated Task", priority="Low")
    assert success == True
    updated_task = tm.get_task_by_id(1)
    assert updated_task.title == "Updated Task"
    assert updated_task.priority == "Low"
    print("SUCCESS: Task update works")

    # Test toggling completion
    original_status = updated_task.completed
    success = tm.toggle_task_completion(1)
    assert success == True
    toggled_task = tm.get_task_by_id(1)
    assert toggled_task.completed != original_status
    print("SUCCESS: Task completion toggle works")

    # Test deleting a task
    success = tm.delete_task(1)
    assert success == True
    assert len(tm.get_all_tasks()) == 0
    assert tm.get_task_by_id(1) is None
    print("SUCCESS: Task deletion works")

    # Test filtering
    tm.add_task("Task 1", "Description", "High", "Work")
    tm.add_task("Task 2", "Description", "Low", "Personal")
    tm.add_task("Task 3", "Description", "High", "Work")

    work_tasks = tm.filter_tasks_by_category("Work")
    assert len(work_tasks) == 2
    print("SUCCESS: Category filtering works")

    high_tasks = tm.filter_tasks_by_priority("High")
    assert len(high_tasks) == 2
    print("SUCCESS: Priority filtering works")

    return True


def main():
    """Run all tests."""
    print("Running basic functionality tests...\n")

    task_test_result = test_task_creation()
    manager_test_result = test_task_manager()

    if task_test_result and manager_test_result:
        print("\nSUCCESS: All tests passed!")
        return True
    else:
        print("\nERROR: Some tests failed!")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)