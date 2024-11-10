# src/utils/file_management.py

import os
import pandas as pd
import json
import logging

class FileManager:
    """
    A class for handling file operations.
    """

    @staticmethod
    def read_csv(file_path):
        """
        Read a CSV file into a DataFrame.

        Parameters:
        - file_path (str): The path to the CSV file.

        Returns:
        - pd.DataFrame: The DataFrame containing the data.
        """
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            df = pd.read_csv(file_path)
            logging.info(f"Successfully read CSV file: {file_path}")
            return df
        except Exception as e:
            logging.error(f"Error reading CSV file: {e}")
            raise

    @staticmethod
    def write_csv(dataframe, file_path):
        """
        Write a DataFrame to a CSV file.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to write.
        - file_path (str): The path to save the CSV file.
        """
        try:
            dataframe.to_csv(file_path, index=False)
            logging.info(f"Successfully wrote DataFrame to CSV file: {file_path}")
        except Exception as e:
            logging.error(f"Error writing CSV file: {e}")
            raise

    @staticmethod
    def read_json(file_path):
        """
        Read a JSON file into a dictionary.

        Parameters:
        - file_path (str): The path to the JSON file.

        Returns:
        - dict: The dictionary containing the data.
        """
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
            logging.info(f"Successfully read JSON file: {file_path}")
            return data
        except Exception as e:
            logging.error(f"Error reading JSON file: {e}")
            raise

    @staticmethod
    def write_json(data, file_path):
        """
        Write a dictionary to a JSON file.

        Parameters:
        - data (dict): The data to write.
        - file_path (str): The path to save the JSON file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            logging.info(f"Successfully wrote data to JSON file: {file_path}")
        except Exception as e:
            logging.error(f"Error writing JSON file: {e}")
            raise

    @staticmethod
    def file_exists(file_path):
        """
        Check if a file exists.

       Parameters:
        - file_path (str): The path to the file.

        Returns:
        - bool: True if the file exists, False otherwise.
        """
        exists = os.path.exists(file_path)
        logging.info(f"Checked existence of file: {file_path} - Exists: {exists}")
        return exists
