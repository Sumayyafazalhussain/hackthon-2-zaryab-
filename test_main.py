import unittest
from unittest.mock import patch
from io import StringIO
import sys
from main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        # Redirect stdout to a string buffer
        stdout_capture = StringIO()
        sys.stdout = stdout_capture

        # Mock command-line arguments
        with patch.object(sys, 'argv', ['main.py', 'test_command']):
            main()

        # Get the output and restore stdout
        output = stdout_capture.getvalue().strip()
        sys.stdout = sys.__stdout__

        # Assert the output is correct
        self.assertEqual(output, "Executing command: test_command")

if __name__ == '__main__':
    unittest.main()
