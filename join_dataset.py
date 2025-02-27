import pandas as pd

def find_diff_columns(file1, file2):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Find the columns that are different between the two files
    diff_columns = set(df1.columns).symmetric_difference(set(df2.columns))
    
    print("Different columns:", diff_columns)
    return diff_columns


def merge_csv_files(file1, file2, output_file):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Merge both files import pandas as pd

def merge_csv_files(file1, file2, output_file):
    # Read the CSV files
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    
    # Merge both files using outer join to keep all columns
    merged_df = pd.merge(df1, df2, how='outer')
    
    # Check if the merged DataFrame is not empty before saving
    if not merged_df.empty:
        merged_df.to_csv(output_file, index=False)
        print(f"Merged file saved as {output_file}")
    else:
        print("Merged file is empty. No file was created.")

# Example usage
merge_csv_files('file1.csv', 'file2.csv', 'merged_output.csv')

