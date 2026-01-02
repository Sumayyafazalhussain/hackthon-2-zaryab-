import unittest
import os
from utils.file_util import read_file, write_file

class TestFileUtil(unittest.TestCase):
    def test_read_write_file(self):
        test_file = "test.txt"
        test_content = "Hello, world!"

        # Write content to the file
        write_file(test_file, test_content)

        # Read the content back
        content = read_file(test_file)

        # Assert the content is correct
        self.assertEqual(content, test_content)

        # Clean up the test file
        os.remove(test_file)

if __name__ == '__main__':
    unittest.main()
