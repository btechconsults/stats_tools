import pandas as pd

# Load CSV file
df = pd.read_csv('your_file.csv', dtype={'column1': str, 'column2': int})  # Specify types directly

# Convert columns explicitly (for more control)
df['date_column'] = pd.to_datetime(df['date_column'], errors='coerce')  # Convert to datetime
df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')  # Convert to number
df['boolean_column'] = df['boolean_column'].astype(bool)  # Convert to boolean

# Save back to CSV
df.to_csv('fixed_file.csv', index=False)

print("Data types fixed and saved to 'fixed_file.csv'")
