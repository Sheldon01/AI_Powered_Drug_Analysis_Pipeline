import pandas as pd

# Load the data
file_path = 'output/processed_data.csv'
data = pd.read_csv(file_path)

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Calculate percentage of missing data
missing_percentage = (missing_values / len(data)) * 100
print("\nPercentage of missing values:")
print(missing_percentage)

# Example: Drop columns with more than 50% missing values
threshold = 50  # Adjust this as needed
columns_to_drop = missing_percentage[missing_percentage > threshold].index
data = data.drop(columns=columns_to_drop)
print(f"\nDropped columns: {columns_to_drop}")
