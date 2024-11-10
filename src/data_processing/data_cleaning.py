# src/data_processing/data_cleaning.py

import logging
import pandas as pd
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataCleaner:
    """
    Class for cleaning and preprocessing data.
    """

    def __init__(self, dataframe):
        """
        Initialize the DataCleaner with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to clean.
        """
        if not isinstance(dataframe, pd.DataFrame):
            logging.error("Provided input is not a pandas DataFrame.")
            raise ValueError("Input must be a pandas DataFrame.")
        
        self.dataframe = dataframe
        logging.info("Initialized DataCleaner.")

    def remove_duplicates(self):
        """Remove duplicate rows from the DataFrame."""
        initial_count = len(self.dataframe)
        self.dataframe = self.dataframe.drop_duplicates()
        logging.info(f"Removed {initial_count - len(self.dataframe)} duplicate rows.")

    def fill_missing_values(self, strategy='mean', fill_value=None):
        """
        Fill missing values in the DataFrame.

        Parameters:
        - strategy (str): The strategy to use for filling missing values ('mean', 'median', 'mode', or 'constant').
        - fill_value (any): The value to use if strategy is 'constant'.
        """
        for column in self.dataframe.columns:
            if self.dataframe[column].isnull().any():
                if strategy == 'mean':
                    self.dataframe[column].fillna(self.dataframe[column].mean(), inplace=True)
                elif strategy == 'median':
                    self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)
                elif strategy == 'mode':
                    self.dataframe[column].fillna(self.dataframe[column].mode()[0], inplace=True)
                elif strategy == 'constant' and fill_value is not None:
                    self.dataframe[column].fillna(fill_value, inplace=True)
                else:
                    logging.warning(f"Unknown strategy '{strategy}' for column '{column}'. No action taken.")
                    continue
                logging.info(f"Filled missing values in column '{column}' using '{strategy}' strategy.")

    def normalize_data(self, method='z-score'):
        """
        Normalize numerical columns in the DataFrame.

        Parameters:
        - method (str): The normalization method ('z-score' or 'min-max').
        """
        numeric_cols = self.dataframe.select_dtypes(include=['float64', 'int']).columns
        if method == 'z-score':
            self.dataframe[numeric_cols] = (self.dataframe[numeric_cols] - self.dataframe[numeric_cols].mean()) / self.dataframe[numeric_cols].std()
            logging.info("Normalized numerical columns using z-score normalization.")
        elif method == 'min-max':
            self.dataframe[numeric_cols] = (self.dataframe[numeric_cols] - self.dataframe[numeric_cols].min()) / (self.dataframe[numeric_cols].max() - self.dataframe[numeric_cols].min())
            logging.info("Normalized numerical columns using min-max normalization.")
        else:
            logging.warning(f"Unknown normalization method '{method}'. No action taken.")

    def remove_outliers(self, threshold=1.5):
        """
        Remove outliers from numerical columns based on the IQR method.

        Parameters:
        - threshold (float): The multiplier for the IQR to define outliers.
        """
        numeric_cols = self.dataframe.select_dtypes(include=['float64', 'int']).columns
        for column in numeric_cols:
            Q1 = self.dataframe[column].quantile(0.25)
            Q3 = self.dataframe[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            initial_count = len(self.dataframe)
            self.dataframe = self.dataframe[(self.dataframe[column] >= lower_bound) & (self.dataframe[column] <= upper_bound)]
            logging.info(f"Removed {initial_count - len(self.dataframe)} outliers from column '{column}'.")

    def get_cleaned_data(self):
        """Return the cleaned DataFrame."""
        logging.info("Returning cleaned DataFrame.")
        return self.dataframe

    def save_cleaned_data(self, file_path, file_format='csv'):
        """
        Save the cleaned DataFrame to a file.

        Parameters:
        - file_path (str): The path to save the cleaned data.
        - file_format (str ): The format to save the data ('csv' or 'excel').
        """
        try:
            if file_format == 'csv':
                self.dataframe.to_csv(file_path, index=False)
                logging.info(f"Cleaned data saved to {file_path} in CSV format.")
            elif file_format == 'excel':
                self.dataframe.to_excel(file_path, index=False)
                logging.info(f"Cleaned data saved to {file_path} in Excel format.")
            else:
                logging.error(f"Unsupported file format: {file_format}. Data not saved.")
        except Exception as e:
            logging.error(f"Error saving cleaned data: {e}")
