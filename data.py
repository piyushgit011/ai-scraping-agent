import json
import pandas as pd

# Path to your JSON file
file_path = 'output/store1.json'

# Load JSON data from a file
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Assuming your data is under the 'Listings' key
df = pd.DataFrame(json_data['Listings'])

# Display the DataFrame
excel_output_path = "output/store1.xlsx"
df.to_excel(excel_output_path, index=False)
