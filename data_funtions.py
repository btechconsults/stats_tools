import pandas as pd

# use means to fill in missing values
# some columns are not numeric, only calculate mean on numeric columns
# by using .mean(numeric_only=True)
df.fillna(df.mean(numeric_only=True), inplace=True)

# confirm your correction with info()
df.info()

# write new csv file" om new datasets for next section
df_08 = pd.read_csv("datafile1") # ('data_08_v1.csv')
df_08.head(2)
# write new csv file om new datasets for next section
df_08.to_csv("datafile2", index=False)
# print info new csv file om new datasets for next section
print(df_08.head(2))

# Apply lambda function to modify labels
labels = list(map(lambda x: x.lower().replace(" ", "_"), labels))
print(labels)
labels = ["Customer ID", "Order Date", "Product Name", "Total Amount"]

# Query datasets 
df = pd.read_csv("datafile1") 
df_2wd = df[df["drive"] == "2WD"]

# Query rows where 'column_name' equals 'some_value'
filtered_df = df.query("column_name == 'some_value'")

# Display the result
print(filtered_df)

# Load the CSV file
# Drop the column (replace 'column_name' with the actual column name)

file_path = "your_file.csv"  # Change this to your actual file path
df = pd.read_csv(file_path)
df.drop(columns=['column_name'], inplace=True)
# Save the modified CSV
df.to_csv("modified_file.csv", index=False)

print("Column dropped successfully and saved as 'modified_file.csv'")

df['B'].str.extract('(\d+)').astype(int)
