import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import sys
import os
from main import main
from utils.file_util import read_file # Import read_file to verify written content

class TestMain(unittest.TestCase):
    def setUp(self):
        # Create a dummy file for testing read/delete
        with open("test_file.txt", "w") as f:
            f.write("Hello, World!")
        # Create a dummy file for testing write (will be overwritten)
        with open("write_test_file.txt", "w") as f:
            f.write("Initial content.")
        # Create a file for permission denied tests
        # This file will be removed in tearDown.
        # Permissions are usually tested by attempting to write to a read-only location
        # or by mocking the open function to raise PermissionError.

    def tearDown(self):
        # Clean up dummy files
        if os.path.exists("test_file.txt"):
            os.remove("test_file.txt")
        if os.path.exists("write_test_file.txt"):
            os.remove("write_test_file.txt")
        if os.path.exists("new_file.txt"): # Clean up file created by write test
            os.remove("new_file.txt")
        if os.path.exists("temp_permission_denied.txt"):
            os.remove("temp_permission_denied.txt")
        if os.path.exists("file_to_delete.txt"): # Clean up file created by delete test
            os.remove("file_to_delete.txt")

    def capture_output(self, args):
        stdout_capture = StringIO()
        stderr_capture = StringIO()
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture
        with patch.object(sys, 'argv', ['main.py'] + args):
            try:
                main()
            except SystemExit as e:
                # argparse exits with SystemExit, we need to catch it
                # and check the exit code
                self.assertEqual(e.code, 2) # Typically 2 for argument parsing errors

        output = stdout_capture.getvalue().strip() + stderr_capture.getvalue().strip()
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
        return output

    @patch('sys.exit')
    def test_main(self, mock_exit):
        output = self.capture_output(['test_command'])
        # Expecting argparse to print help and then exit
        mock_exit.assert_called_with(2) # argparse exits with 2 for argument errors
        self.assertIn("usage: main.py", output)
        self.assertIn("error: unrecognized arguments: test_command", output)

    def test_read_valid_file(self):
        output = self.capture_output(['read', 'test_file.txt'])
        self.assertEqual(output, "Hello, World!")

    def test_read_non_existent_file(self):
        output = self.capture_output(['read', 'non_existent_file.txt'])
        self.assertEqual(output, "Error: File not found at non_existent_file.txt")

    @patch('builtins.open', new_callable=mock_open)
    def test_read_permission_denied_file(self, mock_file):
        # Configure mock_file to raise PermissionError on read
        mock_file.side_effect = PermissionError
        output = self.capture_output(['read', 'temp_permission_denied.txt'])
        self.assertEqual(output, "Error: Permission denied for file at temp_permission_denied.txt")
        mock_file.side_effect = None # Ensure that the original open is restored for other tests

    def test_write_new_file(self):
        file_path = "new_file.txt"
        content = "This is new content."
        output = self.capture_output(['write', file_path, content])
        self.assertEqual(output, f"Successfully wrote to file: {file_path}")
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(read_file(file_path), content)

    def test_write_overwrite_file(self):
        file_path = "write_test_file.txt"
        content = "Overwritten content."
        output = self.capture_output(['write', file_path, content])
        self.assertEqual(output, f"Successfully wrote to file: {file_path}")
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(read_file(file_path), content)

    @patch('builtins.open', new_callable=mock_open)
    def test_write_permission_denied_file(self, mock_file):
        mock_file.side_effect = PermissionError
        output = self.capture_output(['write', 'temp_permission_denied.txt', 'some content'])
        self.assertEqual(output, "Error: Permission denied for file at temp_permission_denied.txt")
        mock_file.side_effect = None

    def test_delete_existing_file(self):
        # Create a file to be deleted
        file_path = "file_to_delete.txt"
        with open(file_path, "w") as f:
            f.write("Content to be deleted.")
        self.assertTrue(os.path.exists(file_path))

        output = self.capture_output(['delete', file_path])
        self.assertEqual(output, f"Successfully deleted file: {file_path}")
        self.assertFalse(os.path.exists(file_path))

    def test_delete_non_existent_file(self):
        output = self.capture_output(['delete', 'non_existent_delete_file.txt'])
        self.assertEqual(output, "Error: File not found at non_existent_delete_file.txt")

    @patch('os.remove')
    def test_delete_permission_denied_file(self, mock_os_remove):
        mock_os_remove.side_effect = PermissionError
        output = self.capture_output(['delete', 'temp_permission_denied.txt'])
        self.assertEqual(output, "Error: Permission denied for file at temp_permission_denied.txt")
        mock_os_remove.side_effect = None

if __name__ == '__main__':
    unittest.main()

