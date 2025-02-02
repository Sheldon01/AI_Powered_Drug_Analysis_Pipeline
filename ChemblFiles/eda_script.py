import pandas as pd

# Correct file path for the CSV
file_path = 'output/processed_data.csv'

# Load the data
data = pd.read_csv(file_path)

# Preview the first few rows
print(data.head())
print(data.info())
