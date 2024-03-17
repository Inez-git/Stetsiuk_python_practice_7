import unittest
from app.io.input import input_from_file, input_from_file_with_pandas


class TestInput(unittest.TestCase):
    def test_input_from_file_exists(self):
        """
        Checks if the function input_from_file exists.
        """
        self.assertTrue(callable(input_from_file))

    def test_input_from_file_returns_string(self):
        """
        Checks if the function input_from_file returns a string when given a valid file path.
        """
        file_path = "./data/test_file.txt"
        self.assertTrue(isinstance(input_from_file(file_path), str))

    def test_input_from_file_with_invalid_file(self):
        """
        Checks if the function input_from_file returns the correct error message when given an invalid file path.
        """
        file_path = "no_such_file.txt"
        self.assertEqual(input_from_file(file_path), "File not found")

    def test_input_from_file_with_pandas_exists(self):
        """
        Checks if the function input_from_file_with_pandas exists.
        """
        self.assertTrue(callable(input_from_file_with_pandas))

    def test_input_from_file_with_pandas_with_invalid_file(self):
        """
        Checks if the function input_from_file_with_pandas returns the correct error message
        when given an invalid file path.
        """
        file_path = "no_such_file.txt"
        self.assertEqual(input_from_file_with_pandas(file_path), "File not found")


if __name__ == '__main__':
    unittest.main()
