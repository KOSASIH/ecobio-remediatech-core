# src/data_processing/__init__.py

import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dynamically import modules
__all__ = []

def dynamic_import(module_name):
    """
    Dynamically import a module and add it to the __all__ list.
    
    Parameters:
    - module_name (str): The name of the module to import.
    
    Returns:
    - module: The imported module.
    """
    try:
        module = __import__(module_name, fromlist=[''])
        __all__.append(module_name)
        logging.info(f"Successfully imported module: {module_name}")
        return module
    except ImportError as e:
        logging.error(f"Error importing module '{module_name}': {e}")
        return None

# List of modules to import
modules = ['data_cleaning', 'statistical_analysis', 'visualization']

for module in modules:
    dynamic_import(f".{module}")

# Importing classes for easier access
from .data_cleaning import DataCleaner
from .statistical_analysis import StatisticalAnalyzer
from .visualization import DataVisualizer

# Expose the classes in the package
__all__ += ['DataCleaner', 'StatisticalAnalyzer', 'DataVisualizer']

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A package for advanced data processing and analysis."
