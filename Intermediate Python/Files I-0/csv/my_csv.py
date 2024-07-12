import pandas as pd

# Define the path to your CSV file
csv_file_path = 'sample.csv'

# Creating a sample CSV file (for demonstration purposes)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Favorite Color': ['Red', 'Blue', 'Green']
}

# Convert the data dictionary to a DataFrame
df = pd.DataFrame(data)

# Writing the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)
print(f"CSV file written to {csv_file_path}")

# Reading the CSV file into a DataFrame
df_read = pd.read_csv(csv_file_path)

# Display the content of the CSV file
print("Content of the CSV file:")
print(df_read)
