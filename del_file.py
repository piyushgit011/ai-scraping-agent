import os

# Directory containing the Excel files
directory = ''

# Loop through the files in the directory
for file in os.listdir(directory):
    # Check for .xlsx files
    if file.endswith('.csv'):
        file_path = os.path.join(directory, file)
        # Delete the file
        os.remove(file_path)
        print(f"Deleted {file_path}")
