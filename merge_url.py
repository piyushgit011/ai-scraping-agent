import pandas as pd

# Define the file path
file_path = 'final_merged_data.csv'  # Adjust the file path as needed
output_path = 'dubai_villas.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Function to modify the URLs
def modify_url(url):
    if pd.notna(url) and url.startswith('/en'):
        return "https://www.propertyfinder.ae" + url
    return url

# Apply the function to the "URL of Property" column
df['URL of Property'] = df['URL of Property'].apply(modify_url)

# Save the modified DataFrame back to a CSV file
df.to_csv(output_path, index=False)
