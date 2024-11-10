# examples/example_field_test.py

import logging
import random
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FieldTest:
    def __init__(self, location):
        self.location = location
        self.data = []

    def conduct_test(self):
        """Conduct the field test and collect data."""
        logging.info(f"Conducting field test at {self.location}")
        for _ in range(5):  # Simulate 5 data collection points
            measurement = self.collect_data()
            self.data.append(measurement)
            logging.info(f"Collected data: {measurement}")
            time.sleep(2)  # Simulate time delay for data collection

        self.analyze_results()

    def collect_data(self):
        """Simulate data collection from the field."""
        return{
            "timestamp": time.time(),
            "value": random.uniform(0, 100)  # Simulated measurement
        }

    def analyze_results(self):
        """Analyze the collected results."""
        if self.data:
            average_value = sum(d['value'] for d in self.data) / len(self.data)
            logging.info(f"Average value from field test at {self.location}: {average_value:.2f}")
        else:
            logging.warning("No data collected during the field test.")

if __name__ == "__main__":
    field_test = FieldTest(location="Test Site A")
    field_test.conduct_test()
