# tests/test_data_processing.py

import unittest
import pandas as pd
import os
from unittest.mock import patch
from src.utils.file_management import FileManager

# Configure logging for the test module
import logging
logging.basicConfig(level=logging.INFO)

class TestDataProcessing(unittest.TestCase):
    
    def setUp(self):
        """Set up test data and environment."""
        self.df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        self.csv_file = 'test_data.csv'
        self.json_file = 'test_data.json'
        logging.info("Setting up test data.")

    def tearDown(self):
        """Clean up after tests."""
        logging.info("Tearing down test data.")
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_write_and_read_csv(self):
        """Test writing and reading CSV."""
        FileManager.write_csv(self.df, self.csv_file)
        df_read = FileManager.read_csv(self.csv_file)
        pd.testing.assert_frame_equal(self.df, df_read)
        logging.info("CSV write and read test passed.")

    def test_write_and_read_json(self):
        """Test writing and reading JSON."""
        data = self.df.to_dict(orient='records')
        FileManager.write_json(data, self.json_file)
        data_read = FileManager.read_json(self.json_file)
        self.assertEqual(data, data_read)
        logging.info("JSON write and read test passed.")

    def test_file_exists(self):
        """Test file existence check."""
        FileManager.write_csv(self.df, self.csv_file)
        exists = FileManager.file_exists(self.csv_file)
        self.assertTrue(exists)
        logging.info("File existence check test passed.")

    def test_read_non_existent_file(self):
        """Test reading a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            FileManager.read_csv('non_existent_file.csv')
        logging.info("Non-existent file read test passed.")

    def test_write_invalid_data(self):
        """Test writing invalid data to CSV."""
        with self.assertRaises(ValueError):
            FileManager.write_csv(None, self.csv_file)  # Attempt to write None
        logging.info("Invalid data write test passed.")

    def test_read_invalid_json(self):
        """Test reading invalid JSON data."""
        with open(self.json_file, 'w') as f:
            f.write("invalid json")
        
        with self.assertRaises(json.JSONDecodeError):
            FileManager.read_json(self.json_file)
        logging.info("Invalid JSON read test passed.")

if __name__ == '__main__':
    unittest.main()
