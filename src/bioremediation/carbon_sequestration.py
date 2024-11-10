# src/bioremediation/carbon_sequestration.py

import logging
import pandas as pd
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CarbonSequestration:
    """
    Class for managing carbon sequestration projects and analysis.
    """

    def __init__(self, project_name):
        self.project_name = project_name
        self.data_records = pd.DataFrame(columns=['date', 'carbon_sequestered', 'method', 'location'])
        logging.info(f"Initialized CarbonSequestration project: {self.project_name}")

    def record_sequestration(self, date, carbon_sequestered, method, location):
        """
        Record a carbon sequestration event.
        
        Parameters:
        - date (str): The date of the sequestration event.
        - carbon_sequestered (float): The amount of carbon sequestered (in tons).
        - method (str): The method used for carbon sequestration.
        - location (str): The location of the sequestration.
        """
        logging.info(f"Recording sequestration for project '{self.project_name}' on {date}")
        
        # Validate input data
        if not self.validate_input_data(date, carbon_sequestered, method, location):
            logging.error("Input data validation failed.")
            return None

        # Append the new record to the DataFrame
        new_record = {
            'date': pd.to_datetime(date),
            'carbon_sequestered': carbon_sequestered,
            'method': method,
            'location': location
        }
        self.data_records = self.data_records.append(new_record, ignore_index=True)
        logging.info(f"Recorded sequestration: {new_record}")

    def validate_input_data(self, date, carbon_sequestered, method, location):
        """
        Validate the input data for recording a sequestration event.
        
        Parameters:
        - date (str): The date of the sequestration event.
        - carbon_sequestered (float): The amount of carbon sequestered (in tons).
        - method (str): The method used for carbon sequestration.
        - location (str): The location of the sequestration.
        
        Returns:
        - bool: True if valid, False otherwise.
        """
        if not isinstance(carbon_sequestered, (int, float)) or carbon_sequestered < 0:
            logging.warning("Carbon sequestered must be a non-negative number.")
            return False
        if not isinstance(date, str):
            logging.warning("Date must be a string in 'YYYY-MM-DD' format.")
            return False
        if not isinstance(method, str) or not method:
            logging.warning("Method must be a non-empty string.")
            return False
        if not isinstance(location, str) or not location:
            logging.warning("Location must be a non-empty string.")
            return False
        return True

    def analyze_sequestration_data(self):
        """
        Analyze the carbon sequestration data.
        
        Returns:
        - dict: A summary of the analysis results.
        """
        logging.info("Analyzing carbon sequestration data...")
        if self.data_records.empty:
            logging.warning("No data records available for analysis.")
            return None
        
        total_sequestered = self.data_records['carbon_sequestered'].sum()
        analysis_summary = {
            "total_records": len(self.data_records),
            "total_carbon_sequestered": total_sequestered,
            "average_sequestration": self.data_records['carbon_sequestered'].mean()
        }
        logging.info(f"Carbon sequestration analysis: {analysis_summary}")
        return analysis_summary

    def fetch_external_carbon_data(self, endpoint):
        """
        Fetch external carbon data from an API.
        
        Parameters:
        - endpoint (str): The API endpoint to fetch data from.
        
        Returns:
        - dict: The fetched data or None if an error occurs.
        """
        logging.info(f"Fetching external carbon data from: {endpoint}")
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched external carbon data: {data}")
            return data
        except requests.RequestException as e:
            logging.error(f"Error fetching external carbon data: {e}")
            return None
