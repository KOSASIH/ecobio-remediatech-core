# src/data_processing/statistical_analysis.py

import logging
import pandas as pd
import numpy as np
from scipy import stats

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StatisticalAnalyzer:
    """
    Class for performing statistical analysis on data.
    """

    def __init__(self, dataframe):
        """
        Initialize the StatisticalAnalyzer with a DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): The DataFrame to analyze.
        """
        if not isinstance(dataframe, pd.DataFrame):
            logging.error("Provided input is not a pandas DataFrame.")
            raise ValueError("Input must be a pandas DataFrame.")
        
        self.dataframe = dataframe
        logging.info("Initialized StatisticalAnalyzer.")

    def descriptive_statistics(self):
        """Calculate and return descriptive statistics."""
        stats_summary = self.dataframe.describe()
        logging.info("Calculated descriptive statistics.")
        return stats_summary

    def correlation_matrix(self):
        """Calculate and return the correlation matrix."""
        correlation = self.dataframe.corr()
        logging.info("Calculated correlation matrix.")
        return correlation

    def t_test(self, group1, group2):
        """
        Perform a t-test between two groups.

        Parameters:
        - group1 (str): The name of the first group column.
        - group2 (str): The name of the second group column.

        Returns:
        - dict: T-test results including statistic and p-value.
        """
        if group1 not in self.dataframe.columns or group2 not in self.dataframe.columns:
            logging.error(f"One or both groups '{group1}' and '{group2}' not found in DataFrame.")
            raise ValueError("Both group columns must exist in the DataFrame.")
        
        t_stat, p_value = stats.ttest_ind(self.dataframe[group1].dropna(), self.dataframe[group2].dropna())
        logging.info(f"Performed t-test between '{group1}' and '{group2}'.")
        return {'t_statistic': t_stat, 'p_value': p_value}

    def chi_square_test(self, column1, column2):
        """
        Perform a Chi-Square test of independence between two categorical variables.

        Parameters:
        - column1 (str): The name of the first categorical column.
        - column2 (str): The name of the second categorical column.

        Returns:
        - dict: Chi-Square test results including statistic and p-value.
        """
        if column1 not in self.dataframe.columns or column2 not in self.dataframe.columns:
            logging.error(f"One or both columns '{column1}' and '{column2}' not found in DataFrame.")
            raise ValueError("Both columns must exist in the DataFrame.")
        
        contingency_table = pd.crosstab(self.dataframe[column1], self.dataframe[column2])
        chi2_stat, p_value, dof, expected = stats.chi2_contingency(contingency_table)
        logging.info(f"Performed Chi-Square test between '{column1}' and '{column2}'.")
        return {'chi2_statistic': chi2_stat, 'p_value': p_value, 'degrees_of_freedom': dof}

    def anova_test(self, dependent_var, independent_var):
        """
        Perform a one-way ANOVA test.

        Parameters:
        - dependent_var (str): The name of the dependent variable.
        - independent_var (str): The name of the independent variable.

        Returns:
        - dict: ANOVA test results including F-statistic and p-value.
        """
        if dependent_var not in self.dataframe.columns or independent_var not in self.dataframe.columns:
            logging.error(f"One or both variables '{dependent_var}' and '{independent_var}' not found in DataFrame.")
            raise ValueError("Both variables must exist in the DataFrame.")
        
        groups = [group[1].values for group in self.dataframe.groupby(independent_var)[dependent_var]]
        f_stat, p_value = stats.f_oneway(*groups)
        logging.info(f"Performed ANOVA test for '{dependent_var}' by '{independent_var}'.")
        return {'f_statistic': f_stat, 'p_value': p_value}

    def get_summary(self):
        """Return a summary of the statistical analysis methods available."""
        summary = {
            'methods': [
                'Descriptive Statistics',
                'Correlation Matrix',
                'T-Test',
                'Chi-Square Test',
                'ANOVA Test'
            ],
            'description': 'This class provides various statistical analysis methods for data analysis.'
        logging.info("Returned summary of statistical analysis methods.")
        return summary

    def save_results(self, results, file_path, file_format='json'):
        """
        Save the statistical analysis results to a file.

        Parameters:
        - results (dict): The results to save.
        - file_path (str): The path to save the results.
        - file_format (str): The format to save the results ('json' or 'csv').
        """
        try:
            if file_format == 'json':
                import json
                with open(file_path, 'w') as json_file:
                    json.dump(results, json_file)
                logging.info(f"Results saved to {file_path} in JSON format.")
            elif file_format == 'csv':
                results_df = pd.DataFrame.from_dict(results, orient='index').reset_index()
                results_df.columns = ['Metric', 'Value']
                results_df.to_csv(file_path, index=False)
                logging.info(f"Results saved to {file_path} in CSV format.")
            else:
                logging.error(f"Unsupported file format: {file_format}. Results not saved.")
        except Exception as e:
            logging.error(f"Error saving results: {e}")
