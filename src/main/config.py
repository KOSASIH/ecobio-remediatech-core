# src/main/config.py

import os
import json
import logging

class Config:
    """
    Configuration class to manage application settings.
    """

    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        """
        Load configuration settings from a JSON file.
        """
        if not os.path.exists(self.config_file):
            logging.warning(f"Configuration file {self.config_file} not found. Using default settings.")
            return self.default_settings()
        
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def default_settings(self):
        """
        Return default configuration settings.
        """
        return {
            "log_level": "INFO",
            "database": {
                "host": "localhost",
                "port": 5432,
                "user": "ecobio_user",
                "password": "secure_password",
                "database": "ecobio_db"
            },
            "api": {
                "base_url": "https://api.ecobio-remediatech.org",
                "timeout": 30
            }
        }

    def get(self, key, default=None):
        """
        Get a configuration value by key.
        """
        return self.settings.get(key, default)

# Initialize logging based on configuration
def setup_logging(config: Config):
    log_level = config.get("log_level", "INFO").upper()
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
