import numpy as np
import pandas as pd

class Cleaning:
    # Cleaning
    def __init__(self, dataset, projectID, data_path):
        self.df = pd.read_csv(data_path)
        self.projectID = projectID


    def replace_mean(df):
# Get the column headers as a list
        headers = df.columns.tolist()
        headers = headers[2:]  # Removes the first two items

        # Update all missing mean data
        for column in headers:
            mean = df[column].mean
            print(f" {column}: {mean}")
            df[column].fillna(mean, inplace=True)
            print(f"Replace {column}: {mean}")
        
    # rename_lablel
    def rename_lablel(self, df):
        # Get the column headers as a list
        # remove "_mean" from column names
        new_labels = []
        for col in df.columns:
            if '_mean' in col:
                new_labels.append(col[:-5])  # exclude last 5 characters
            else:
                new_labels.append(col)

        return new_labels