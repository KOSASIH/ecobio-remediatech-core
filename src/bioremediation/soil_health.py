# src/bioremediation/soil_health.py

import logging
import pandas as pd
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SoilHealthAssessment:
    """
    Class for managing soil health assessments and analysis.
    """

    def __init__(self, site_name):
        self.site_name = site_name
        self.assessment_records = pd.DataFrame(columns=['date', 'pH', 'moisture_content', 'organic_matter', 'nutrient_levels'])
        logging.info(f"Initialized SoilHealthAssessment for site: {self.site_name}")

    def record_assessment(self, date, pH, moisture_content, organic_matter, nutrient_levels):
        """
        Record a soil health assessment.
        
        Parameters:
        - date (str): The date of the assessment.
        - pH (float): The pH level of the soil.
        - moisture_content (float): The moisture content of the soil (in %).
        - organic_matter (float): The organic matter content (in %).
        - nutrient_levels (dict): A dictionary containing nutrient levels (e.g., N, P, K).
        """
        logging.info(f"Recording soil health assessment for site '{self.site_name}' on {date}")
        
        # Validate input data
        if not self.validate_input_data(date, pH, moisture_content, organic_matter, nutrient_levels):
            logging.error("Input data validation failed.")
            return None

        # Append the new record to the DataFrame
        new_record = {
            'date': pd.to_datetime(date),
            'pH': pH,
            'moisture_content': moisture_content,
            'organic_matter': organic_matter,
            'nutrient_levels': nutrient_levels
        }
        self.assessment_records = self.assessment_records.append(new_record, ignore_index=True)
        logging.info(f"Recorded assessment: {new_record}")

    def validate_input_data(self, date, pH, moisture_content, organic_matter, nutrient_levels):
        """
        Validate the input data for recording a soil health assessment.
        
        Parameters:
        - date (str): The date of the assessment.
        - pH (float): The pH level of the soil.
        - moisture_content (float): The moisture content of the soil (in %).
        - organic_matter (float): The organic matter content (in %).
        - nutrient_levels (dict): A dictionary containing nutrient levels (e.g., N, P, K).
        
        Returns:
        - bool: True if valid, False otherwise.
        """
        if not isinstance(pH, (int, float)) or not (0 <= pH <= 14):
            logging.warning("pH must be a number between 0 and 14.")
            return False
        if not isinstance(moisture_content, (int, float)) or moisture_content < 0:
            logging.warning("Moisture content must be a non-negative number.")
            return False
        if not isinstance(organic_matter, (int, float)) or organic_matter < 0:
            logging.warning("Organic matter must be a non-negative number.")
            return False
        if not isinstance(nutrient_levels, dict):
            logging.warning("Nutrient levels must be provided as a dictionary.")
            return False
        return True

    def analyze_assessment_data(self):
        """
        Analyze the soil health assessment data.
        
        Returns:
        - dict: A summary of the analysis results.
        """
        logging.info("Analyzing soil health assessment data...")
        if self.assessment_records.empty:
            logging.warning("No assessment records available for analysis.")
            return None
        
        analysis_summary = {
            "total_assessments": len(self.assessment_records),
            "average_pH": self.assessment_records['pH'].mean(),
            "average_moisture_content": self.assessment_records['moisture_content'].mean(),
            "average_organic_matter": self.assessment_records['organic_matter'].mean(),
            "nutrient_levels": self.assessment_records['nutrient_levels'].apply(pd.Series).mean().to_dict()
        }
        logging.info(f"Soil health assessment analysis: {analysis_summary}")
        return analysis_summary

    def fetch_external_soil_data(self, endpoint):
        """
        Fetch external soil health data from an API.
        
        Parameters:
        - endpoint (str): The API endpoint to fetch data from.
        
        Returns:
        - dict: The fetched data or None if an error occurs.
        """
        logging.info(f"Fetching external soil health data from: {endpoint}")
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched external soil health data: {data}")
            return data
        except requests.RequestException as e:
            logging.error(f"Error fetching external soil health data: {e}")
            return None
