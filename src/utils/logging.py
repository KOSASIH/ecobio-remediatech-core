# src/utils/logging.py

import logging
import os

def setup_logging(log_file='app.log', log_level=logging.INFO):
    """
    Set up logging configuration.

    Parameters:
    - log_file (str): The name of the log file.
    - log_level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
    """
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    log_file_path = os.path.join('logs', log_file)

    logging.basicConfig(
        filename=log_file_path,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'  # Append mode
    )

    # Also log to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logging.getLogger().addHandler(console_handler)
    logging.info("Logging is set up.")
