import pandas as pd

# Define the path to your cleaned_data.csv (relative to the current directory)
csv_file = r"output/cleaned_data.csv"

# Load the CSV file
df = pd.read_csv(csv_file)

# Save the file as Parquet
parquet_file = r"output/cleaned_data.parquet"
df.to_parquet(parquet_file, engine='pyarrow')

print(f"CSV file converted to Parquet and saved at: {parquet_file}")