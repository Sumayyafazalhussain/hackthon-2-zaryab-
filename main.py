"""
Entry point for the Todo In-Memory Console App.

This module serves as the main entry point for the application.
"""

from src.app import TodoApp


def main():
    """
    Main entry point for the application.
    """
    app = TodoApp()
    app.run()


if __name__ == "__main__":
    main()