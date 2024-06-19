import os
import pandas as pd

# Directory containing the Excel files
directory = "final"

# List to hold the dataframes
dfs = []

# Loop through the files in the directory
for file in os.listdir(directory):
    # Check for .xlsx files
    if file.endswith('.csv'):
        file_path = os.path.join(directory, file)
        # Read the Excel file and append to the list
        dfs.append(pd.read_csv(file_path))

# Merge all dataframes
merged_data = pd.concat(dfs, ignore_index=True)

# Define the path for the output CSV file
output_csv_path = 'final_merged_data.csv'

# Save the merged dataframe to a CSV file
merged_data.to_csv(output_csv_path, index=False)

print(f'Merged data has been saved to {output_csv_path}')
