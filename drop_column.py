import pandas as pd

df = pd.read_csv('data/test_dataset.csv')

# Load the CSV file

# Drop the column (replace 'column_name' with the actual column name)
df.drop(columns=['radius_mean'], inplace=True)
# Save the modified CSV
df.to_csv("data/modified_file.csv", index=False)

print("Column dropped successfully and saved as 'modified_file.csv'")


import pandas as pd

# Load the first CSV file
df_08 = pd.read_csv("file1.csv")

# Load the second CSV file
df_18 = pd.read_csv("file2.csv")

# Drop rows with any null values in both datasets
df1_cleaned = df_08.dropna()
df2_cleaned = df_18.dropna()

# Save the cleaned datasets if needed
df1_cleaned.to_csv("df_08__cleaned.csv", index=False)
df2_cleaned.to_csv("fd_18_cleaned.csv", index=False)

# Display the number of rows dropped
print(f"Rows dropped in file1: {len(df1) - len(df1_cleaned)}")
print(f"Rows dropped in file2: {len(df2) - len(df2_cleaned)}")

import pandas as pd

# Load the first CSV file
df1 = pd.read_csv("file1.csv")

# Load the second CSV file
df2 = pd.read_csv("file2.csv")

# Count duplicates in both datasets
duplicates_df1 = df1.duplicated().sum()
duplicates_df2 = df2.duplicated().sum()

# Print the count of duplicate rows
print(f"Duplicate rows in file1: {duplicates_df1}")
print(f"Duplicate rows in file2: {duplicates_df2}")
