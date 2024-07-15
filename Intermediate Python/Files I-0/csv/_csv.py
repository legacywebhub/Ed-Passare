import os
import pandas as pd


# Get the directory of the current script
script_folder = os.path.dirname(os.path.abspath(__file__))

# Define the path to your CSV file in the same directory as the script
csv_file_path = os.path.join(script_folder, 'sample.csv')

# Check if we are in the correct directory
print(f"Current directory: {os.getcwd()}")

# Creating a sample CSV file (for demonstration purposes)
data = {
    'Name': ['Dumebi', 'Utibe', 'Anthony'],
    'Age': [23, 23, 22],
    'Favorite Color': ['Red', 'Blue', 'Green']
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Writing the DataFrame to a CSV file
try:
    df.to_csv(csv_file_path, index=False)
    print(f"CSV file written to {csv_file_path}")
except Exception as e:
    print(f"Failed to write CSV file: {e}")

# Check if the file exists and print its path
if os.path.exists(csv_file_path):
    print(f"File {csv_file_path} exists.")

    # Reading the CSV file into a DataFrame
    df_read = pd.read_csv(csv_file_path)

    # Display the content of the CSV file
    print("Content of the CSV file:")
    print(df_read)
else:
    print(f"File {csv_file_path} does not exist. There was an issue with writing the file.")