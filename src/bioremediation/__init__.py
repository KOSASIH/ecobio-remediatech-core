# bioremediation/__init__.py

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

# Load all bioremediation modules dynamically
bioremediation_modules = load_modules(__package__)

# Expose classes for easier access
__all__ = []
for module_name, module in bioremediation_modules.items():
    for class_name in dir(module):
        if not class_name.startswith('_'):
            cls = getattr(module, class_name)
            if isinstance(cls, type):  # Check if it's a class
                __all__.append(class_name)
                globals()[class_name] = cls

# Example of integrating with an external API for real-time data
def fetch_real_time_data(endpoint):
    """
    Fetch real-time data from an external API for bioremediation.
    """
    logging.info(f"Fetching real-time data from: {endpoint}")
    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched real-time data: {data}")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching real-time data: {e}")
        return None

# Example usage of the real-time data fetching
# Uncomment the following line to fetch data from a hypothetical endpoint
# real_time_data = fetch_real_time_data("https://api.bioremediation.org/data")
