import numpy as np
import pandas as pd
#df = pd.read_csv('cancer_data_means.csv')
df = pd.read_csv('data/breast_cancer_dataset.csv')

# Correlation & Regression
def correlation(col1: str, col2: str):
    """Calculates the Pearson correlation coefficient between two columns."""
    return self.dataset[[col1, col2]].corr().iloc[0, 1] if self.dataset is not None else None

def corr_coef(r):

    # Interpretation of correlation coefficient
    if r == 1:
        print("Perfect positive correlation")
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
        interpretation = "Perfect negative correlation "
    else:
        interpretation = "Unknown correlation"
    
    return interpretation 

# test results 
value = -0.46
xcol = "Age"
ycol = "Stress Level"
result = correlation_coefficient(value)
print(f"Pearson correlation coefficient of {xcol} and {ycol} interpretation is {result}")