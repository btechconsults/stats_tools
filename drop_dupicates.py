import pandas as pd

# Load the first CSV file
df_08 = pd.read_csv("file1.csv")

# Load the second CSV file
df_18 = pd.read_csv("file2.csv")

# Drop duplicate rows
df1_cleaned = df_08.drop_duplicates()
df2_cleaned = df_18.drop_duplicates()

# Save the cleaned datasets
#df1_cleaned.to_csv("file1_cleaned.csv", index=False)
#df2_cleaned.to_csv("file2_cleaned.csv", index=False)

# Print the number of duplicates removed
print(f"Duplicate rows removed from file1: {len(df1) - len(df1_cleaned)}")
print(f"Duplicate rows removed from file2: {len(df2) - len(df2_cleaned)}")
