import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from typing import Callable, Dict, Optional

class Project:
    projectID = 1100
    """
    A base class for managing project metadata, handling datasets from CSV files, 
    and providing statistical functions using Pandas, NumPy, and SciPy.
    """
    def __init__(self, name: str, author: str, course: str, dataset_path: Optional[str] = None):
        """
        Initializes the project with metadata and an optional dataset from a CSV file.

        """
        self.name = name
        self.author = author
        self.course = course
        self.dataset = dataset_path  # Pandas DataFrame
        self.methods: Dict[str, Callable] = {}  # Store functions dynamically
        self.projecID += 1

        # Load dataset if provided
        if dataset_path:
            self.dataset_path = dataset_path
            self.load_dataset(dataset_path)

        # Initialize statistical methods
        self._initialize_statistical_methods()

    def get_summary(self) -> str:
        """Returns a summary of the project."""
        return f"ProjectID: \nProjectID: {self.projectID} {self.name}\nAuthor: {self.author}\nCourse: {self.course}\nDataset Loaded: {self.dataset is not None} \nDataset: {self.dataset_path} "

    def load_dataset(self, file_path: str):
        """Loads a dataset from a CSV file into a Pandas DataFrame."""
        try:
            self.dataset = pd.read_csv(file_path)
            print(f"Dataset loaded successfully from {file_path}")
        except Exception as e:
            print(f"Error loading dataset: {e}")

    def add_method(self, name: str, function: Callable):
        """Dynamically adds a method to the project."""
        self.methods[name] = function

    def list_methods(self):
        """Lists all available statistical methods."""
        return list(self.methods.keys())

    def execute_method(self, name: str, *args, **kwargs):
        """Executes a stored method."""
        if name in self.methods:
            return self.methods[name](*args, **kwargs)
        else:
            raise ValueError(f"Method '{name}' not found.")

    def _initialize_statistical_methods(self):
        """Registers built-in statistical methods."""

        # Basic Statistics
        def describe():
            """Returns a statistical summary of the dataset."""
            return self.dataset.describe() if self.dataset is not None else "No dataset loaded."

        def mean(column: str):
            """Returns the mean of a specified column."""
            return self.dataset[column].mean() if self.dataset is not None else None

        def variance(column: str):
            """Returns the variance of a specified column."""
            return self.dataset[column].var() if self.dataset is not None else None

        def std_dev(column: str):
            """Returns the standard deviation of a specified column."""
            return self.dataset[column].std() if self.dataset is not None else None

        # Correlation & Regression
        def correlation(col1: str, col2: str):
            """Calculates the Pearson correlation coefficient between two columns."""
            return self.dataset[[col1, col2]].corr().iloc[0, 1] if self.dataset is not None else None

        def linear_regression(x_col: str, y_col: str):
            """Performs simple linear regression and returns slope, intercept."""
            if self.dataset is None:
                return None
            x = self.dataset[x_col]
            y = self.dataset[y_col]
            slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
            return {"slope": slope, "intercept": intercept, "r_value": r_value, "p_value": p_value, "std_err": std_err}

        # Probability Distributions
        def normal_distribution(mean: float, std_dev: float, size: int = 1000):
            """Generates a normal distribution and plots a histogram."""
            data = np.random.normal(mean, std_dev, size)
            sns.histplot(data, kde=True)
            plt.title(f"Normal Distribution (μ={mean}, σ={std_dev})")
            plt.show()
            return data

        def binomial_distribution(n: int, p: float, size: int = 1000):
            """Generates a binomial distribution and plots a histogram."""
            data = np.random.binomial(n, p, size)
            sns.histplot(data, kde=False)
            plt.title(f"Binomial Distribution (n={n}, p={p})")
            plt.show()
            return data

        def poisson_distribution(lam: float, size: int = 1000):
            """Generates a Poisson distribution and plots a histogram."""
            data = np.random.poisson(lam, size)
            sns.histplot(data, kde=False)
            plt.title(f"Poisson Distribution (λ={lam})")
            plt.show()
            return data

        # Data Visualization
        def scatter_plot(x_col: str, y_col: str):
            """Creates a scatter plot between two numerical columns."""
            if self.dataset is None:
                print("No dataset loaded.")
                return
            sns.scatterplot(x=self.dataset[x_col], y=self.dataset[y_col])
            plt.title(f"Scatter Plot: {x_col} vs {y_col}")
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()

        def histogram(column: str):
            """Creates a histogram of a specified numerical column."""
            if self.dataset is None:
                print("No dataset loaded.")
                return
            sns.histplot(self.dataset[column], kde=True)
            plt.title(f"Histogram of {column}")
            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.show()

        # Register functions
        self.add_method("describe", describe)
        self.add_method("mean", mean)
        self.add_method("variance", variance)
        self.add_method("standard_deviation", std_dev)
        self.add_method("correlation", correlation)
        self.add_method("linear_regression", linear_regression)
        self.add_method("normal_distribution", normal_distribution)
        self.add_method("binomial_distribution", binomial_distribution)
        self.add_method("poisson_distribution", poisson_distribution)
        self.add_method("scatter_plot", scatter_plot)
        self.add_method("histogram", histogram)
