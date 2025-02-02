import pandas as pd

# Load the processed data
file_path = 'output/processed_data.csv'  # Adjust if needed
data = pd.read_csv(file_path)

# Define outlier thresholds
thresholds = {
    'HBA': 30,  # Example: Maximum value for HBA
    'HBD': 20,  # Maximum value for HBD
    'MW_FREEBASE': 5000  # Maximum value for MW_FREEBASE
}

# Remove outliers
for col, max_value in thresholds.items():
    data = data[data[col] <= max_value]

# Save the cleaned data
data.to_csv('output/cleaned_data.csv', index=False)
print("Outliers removed. Cleaned data saved to 'output/cleaned_data.csv'")
