import pandas as pd


# Find the unique values in cyl for fuel_08_df
def find_unique_value():

    fuel_08_df = pd.read_csv('data_08_v3.csv')
    fuel_18_df = pd.read_csv('data_18_v3.csv')


def correlation_from_csv(file_path, col1, col2):
    """
    Reads a CSV file, computes the Pearson correlation coefficient between two columns,
    and provides an English interpretation.
    
    :param file_path: Path to the CSV file.
    :param col1: Name of the first column.
    :param col2: Name of the second column.
    :return: Tuple (correlation coefficient, interpretation)
    """
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Check if columns exist
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError(f"Columns '{col1}' and/or '{col2}' not found in the CSV file.")
    
    # Drop rows with missing values in the selected columns
    df = df[[col1, col2]].dropna()
    
    # Compute correlation coefficient
    r = df[col1].corr(df[col2])
    
    # Interpretation of correlation coefficient
    if r == 1:
        interpretation = "Perfect positive correlation"
    elif 0.7 <= r < 1:
        interpretation = "Strong positive correlation"
    elif 0.4 <= r < 0.7:
        interpretation = "Moderate positive correlation"
    elif 0.1 <= r < 0.4:
        interpretation = "Weak positive correlation"
    elif r == 0:
        interpretation = "No correlation"
    elif -0.1 > r > -0.4:
        interpretation = "Weak negative correlation"
    elif -0.4 >= r > -0.7:
        interpretation = "Moderate negative correlation"
    elif -0.7 >= r > -1:
        interpretation = "Strong negative correlation"
    elif r == -1:
        interpretation = "Perfect negative correlation"
    else:
        interpretation = "Unknown correlation"

    return r, interpretation

# Example Usage
file_path = "data.csv"  # Replace with your actual CSV file path
col1 = "Height"  # Replace with your column name
col2 = "Weight"  # Replace with your column name

r_value, result = correlation_from_csv(file_path, col1, col2)
print(f"Correlation Coefficient: {r_value:.4f} ({result})")
