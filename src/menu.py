"""
Menu system for the Todo In-Memory Console App.

This module handles displaying menus and getting user input.
"""


def display_main_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("TODO APPLICATION")
    print("="*40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task Complete / Incomplete")
    print("6. Filter Tasks")
    print("7. Exit")
    print("="*40)


def display_filter_menu():
    """
    Display the filter submenu options to the user.
    """
    print("\nFilter Tasks:")
    print("1. Filter by Category")
    print("2. Filter by Priority")
    print("3. Back to Main Menu")


def get_user_choice():
    """
    Get the user's menu choice.
    
    Returns:
        str: The user's choice
    """
    return input("Enter your choice: ").strip()


def get_task_details():
    """
    Prompt user for task details when adding a task.
    
    Returns:
        tuple: (title, description, priority, category)
    """
    print("\nAdd New Task:")
    title = input("Enter task title (required): ").strip()
    
    description = input("Enter task description (optional): ").strip()
    
    while True:
        priority = input("Enter priority (Low/Medium/High) [Medium]: ").strip()
        if not priority:
            priority = "Medium"
        if priority in ["Low", "Medium", "High"]:
            break
        print("Invalid priority. Please enter Low, Medium, or High.")
    
    category = input("Enter category (optional) [General]: ").strip()
    if not category:
        category = "General"
    
    return title, description, priority, category


def get_task_id(prompt="Enter task ID: "):
    """
    Prompt user for a task ID.
    
    Args:
        prompt (str): The prompt to display to the user
    
    Returns:
        int: The task ID, or None if invalid input
    """
    try:
        task_id = int(input(prompt).strip())
        return task_id
    except ValueError:
        print("Invalid input. Please enter a valid task ID (number).")
        return None


def get_task_updates():
    """
    Prompt user for task update details.
    
    Returns:
        dict: Dictionary with update values (only non-empty values)
    """
    print("\nUpdate Task (leave blank to keep current value):")
    
    title = input("Enter new title: ").strip()
    description = input("Enter new description: ").strip()
    
    while True:
        priority = input("Enter new priority (Low/Medium/High): ").strip()
        if not priority:  # Empty input means keep current value
            break
        if priority in ["Low", "Medium", "High"]:
            break
        print("Invalid priority. Please enter Low, Medium, or High.")
    
    category = input("Enter new category: ").strip()
    
    # Only return values that are not empty
    updates = {}
    if title:
        updates['title'] = title
    if description:
        updates['description'] = description
    if priority:
        updates['priority'] = priority
    if category:
        updates['category'] = category
    
    return updates


def get_filter_category():
    """
    Prompt user for category to filter by.
    
    Returns:
        str: The category to filter by
    """
    return input("Enter category to filter by: ").strip()


def get_filter_priority():
    """
    Prompt user for priority to filter by.
    
    Returns:
        str: The priority to filter by
    """
    while True:
        priority = input("Enter priority to filter by (Low/Medium/High): ").strip()
        if priority in ["Low", "Medium", "High"]:
            return priority
        print("Invalid priority. Please enter Low, Medium, or High.")