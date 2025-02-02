import pandas as pd

# File paths based on your directory structure
input_parquet_file = "output/cleaned_data.parquet"
output_parquet_file = "output/refined_cleaned_data.parquet"

# Load the Parquet dataset
data = pd.read_parquet(input_parquet_file)

# Features to drop (retain one feature from highly correlated pairs)
features_to_drop = ['Molecular_Weight', 'ALOGP']  # Adjust based on high correlations

# Drop redundant features
refined_data = data.drop(columns=features_to_drop, errors='ignore')

# Save the refined dataset
refined_data.to_parquet(output_parquet_file, engine='pyarrow')

print(f"Refined dataset saved at: {output_parquet_file}")
