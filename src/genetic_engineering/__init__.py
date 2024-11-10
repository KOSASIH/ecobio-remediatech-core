# src/genetic_engineering/__init__.py

import logging
import pkgutil
import importlib

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_modules(package):
    """
    Dynamically load all modules in the given package.
    """
    modules = {}
    package_name = package.__name__
    logging.info(f"Loading modules from package: {package_name}")

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        full_module_name = f"{package_name}.{module_name}"
        try:
            module = importlib.import_module(full_module_name)
            modules[module_name] = module
            logging.info(f"Loaded module: {full_module_name}")
        except Exception as e:
            logging.error(f"Failed to load module {full_module_name}: {e}")

    return modules

# Load all genetic engineering modules dynamically
genetic_engineering_modules = load_modules(__package__)

# Expose classes and functions for easier access
__all__ = []
for module_name, module in genetic_engineering_modules.items():
    for class_name in dir(module):
        if not class_name.startswith('_'):
            cls = getattr(module, class_name)
            if isinstance(cls, type):  # Check if it's a class
                __all__.append(class_name)
                globals()[class_name] = cls
            elif callable(cls):  # Check if it's a callable function
                __all__.append(class_name)
                globals()[class_name] = cls

# Example of integrating with an external API for genetic data
def fetch_genetic_data(endpoint):
    """
    Fetch genetic data from an external API.
    """
    logging.info(f"Fetching genetic data from: {endpoint}")
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched genetic data: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching genetic data: {e}")
        return None

# Example usage of the genetic data fetching
# Uncomment the following line to fetch data from a hypothetical endpoint
# genetic_data = fetch_genetic_data("https://api.geneticengineering.org/data")
