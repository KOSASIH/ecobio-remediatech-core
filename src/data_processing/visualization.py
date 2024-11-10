# src/data_processing/visualization.py

import logging
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataVisualizer:
    """
    Class for visualizing data using various plotting techniques.
    """

    def __init__(self, dataframe):
        """
        Initialize the DataVisualizer with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to visualize.
        """
        if not isinstance(dataframe, pd.DataFrame):
            logging.error("Provided input is not a pandas DataFrame.")
            raise ValueError("Input must be a pandas DataFrame.")
        
        self.dataframe = dataframe
        logging.info("Initialized DataVisualizer.")

    def plot_histogram(self, column, bins=10, title=None, xlabel=None, ylabel='Frequency'):
        """
        Plot a histogram for a specified column.

        Parameters:
        - column (str): The name of the column to plot.
        - bins (int): The number of bins for the histogram.
        - title (str): The title of the plot.
        - xlabel (str): The label for the x-axis.
        - ylabel (str): The label for the y-axis.
        """
        if column not in self.dataframe.columns:
            logging.error(f"Column '{column}' not found in DataFrame.")
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        plt.figure(figsize=(10, 6))
        sns.histplot(self.dataframe[column], bins=bins, kde=True)
        plt.title(title or f'Histogram of {column}')
        plt.xlabel(xlabel or column)
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
        logging.info(f"Displayed histogram for column '{column}'.")

    def plot_scatter(self, x_column, y_column, title=None, xlabel=None, ylabel=None):
        """
        Plot a scatter plot for two specified columns.

        Parameters:
        - x_column (str): The name of the column for the x-axis.
        - y_column (str): The name of the column for the y-axis.
        - title (str): The title of the plot.
        - xlabel (str): The label for the x-axis.
        - ylabel (str): The label for the y-axis.
        """
        if x_column not in self.dataframe.columns or y_column not in self.dataframe.columns:
            logging.error(f"One or both columns '{x_column}' and '{y_column}' not found in DataFrame.")
            raise ValueError(f"One or both columns '{x_column}' and '{y_column}' not found in DataFrame.")
        
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.dataframe, x=x_column, y=y_column)
        plt.title(title or f'Scatter Plot of {y_column} vs {x_column}')
        plt.xlabel(xlabel or x_column)
        plt.ylabel(ylabel or y_column)
        plt.grid(True)
        plt.show()
        logging.info(f"Displayed scatter plot for '{y_column}' vs '{x_column}'.")

    def plot_boxplot(self, column, title=None, xlabel=None, ylabel='Value'):
        """
        Plot a boxplot for a specified column.

        Parameters:
        - column (str): The name of the column to plot.
        - title (str): The title of the plot.
        - xlabel (str): The label for the x-axis.
        - ylabel (str): The label for the y-axis.
        """
        if column not in self.dataframe.columns:
            logging.error(f"Column '{column}' not found in DataFrame.")
            raise ValueError(f"Column '{column}' not found in DataFrame.")
        
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=self.dataframe[column])
        plt.title(title or f'Boxplot of {column}')
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.show()
        logging.info(f"Displayed boxplot for column '{column}'.")

    def plot_correlation_matrix(self):
        """Plot the correlation matrix as a heatmap."""
        plt.figure(figsize=(12, 8))
        correlation = self.dataframe.corr()
        sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
        plt.title('Correlation Matrix')
        plt.show()
        logging.info("Displayed correlation matrix heatmap.")

    def save_plot(self, filename, format='png'):
        """
        Save the current plot to a file.

        Parameters:
        - filename (str): The name of the file to save the plot.
        - format (str): The format to save the plot ('png', 'jpg', 'pdf', etc.).
        """
        try:
            plt.savefig(f"{filename}.{format}", format=format)
            logging.info(f"Saved plot as {filename}.{format}.")
        except Exception as e:
            logging.error(f"Error saving plot: {e}")

    def get_summary(self):
        """Return a summary of the visualization methods available."""
        summary = {
            'methods': [
                'Histogram',
                'Scatter Plot',
                'Boxplot',
                'Correlation Matrix'
            ],
            'description': 'This class provides various visualization methods for data analysis.'
        }
        logging.info("Returned summary of visualization methods.")
        return summary
