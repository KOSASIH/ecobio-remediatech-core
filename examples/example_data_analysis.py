# examples/example_data_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataAnalysis:
    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data(self):
        """Load data from a JSON file."""
        try:
            self.data = pd.read_json(self.filename)
            logging.info(f"Data loaded from {self.filename}")
        except Exception as e:
            logging.error(f"Error loading data: {e}")

    def analyze_data(self):
        """Perform basic analysis on the data."""
        if self.data is not None:
            logging.info("Performing data analysis...")
            summary = self.data.describe()
            logging.info(f"Data Summary:\n{summary}")
            return summary
        else:
            logging.warning("No data to analyze.")
            return None

    def plot_data(self):
        """Plot the data."""
        if self.data is not None:
            plt.figure(figsize=(10, 5))
            plt.plot(self.data['timestamp'], self.data['value'], marker='o')
            plt.title('Experiment Data Over Time')
            plt.xlabel('Timestamp')
            plt.ylabel('Value')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            logging.warning("No data to plot.")

if __name__ == "__main__":
    analysis = DataAnalysis(filename="Sample Experiment_data.json")
    analysis.load_data()
    analysis.analyze_data()
    analysis.plot_data()
