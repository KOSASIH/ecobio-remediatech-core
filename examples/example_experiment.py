# examples/example_experiment.py

import logging
import random
import time
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Experiment:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.data = []

    def run(self):
        """Run the experiment and collect data."""
        logging.info(f"Starting experiment: {self.name}")
        start_time = time.time()
        
        while time.time() - start_time < self.duration:
            measurement = self.collect_data()
            self.data.append(measurement)
            logging.info(f"Collected data: {measurement}")
            time.sleep(1)  # Simulate time delay for data collection

        logging.info(f"Experiment {self.name} completed.")
        self.save_data()

    def collect_data(self):
        """Simulate data collection."""
        return {
            "timestamp": time.time(),
            "value": random.uniform(0, 100)  # Simulated measurement
        }

    def save_data(self):
        """Save collected data to a JSON file."""
        filename = f"{self.name}_data.json"
        with open(filename, 'w') as f:
            json.dump(self.data, f)
        logging.info(f"Data saved to {filename}")

if __name__ == "__main__":
    experiment = Experiment(name="Sample Experiment", duration=10)
    experiment.run()
