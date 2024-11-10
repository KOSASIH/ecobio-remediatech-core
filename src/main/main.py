# src/main/main.py

import argparse
import logging
from .config import Config, setup_logging

def main():
    # Load configuration
    config = Config()
    setup_logging(config)

    logging.info("Starting EcoBio Remediatech application...")

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="EcoBio Remediatech Application")
    parser.add_argument('--run', choices=['experiment', 'analysis', 'field_test'], required=True,
                        help='Specify the operation to run.')
    parser.add_argument('--config', type=str, default='config.json',
                        help='Path to the configuration file.')
    
    args = parser.parse_args()

    # Load configuration from specified file if provided
    if args.config:
        config = Config(args.config)
        setup_logging(config)

    # Execute the specified operation
    if args.run == 'experiment':
        run_experiment()
    elif args.run == 'analysis':
        run_analysis()
    elif args.run == 'field_test':
        run_field_test()

def run_experiment():
    logging.info("Running experiments...")
    # Placeholder for experiment logic
    # Implement experiment logic here
    logging.info("Experiments completed successfully.")

def run_analysis():
    logging.info("Running data analysis...")
    # Placeholder for analysis logic
    # Implement analysis logic here
    logging.info("Data analysis completed successfully.")

def run_field_test():
    logging.info("Conducting field tests...")
    # Placeholder for field testing logic
    # Implement field testing logic here
    logging.info("Field tests completed successfully.")

if __name__ == "__main__":
    main()
