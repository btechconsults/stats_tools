import pandas as pd

def drop_columns_from_csv(input_file, output_file, columns_to_drop):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Drop specified columns
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    # Save the modified CSV to a new file
    df.to_csv(output_file, index=False)
    print(f"Columns {columns_to_drop} dropped. Saved to {output_file}")

# Example usage
input_csv = "all_alpha_08.csv"
output_csv = "output.csv"
columns_to_remove = ['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG']  # Replace with actual column names
drop_columns_from_csv(input_csv, output_csv, columns_to_remove)

