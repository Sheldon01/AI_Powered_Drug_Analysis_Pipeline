import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Parquet file (adjusted for your file structure)
parquet_file = "output/cleaned_data.parquet"
df = pd.read_parquet(parquet_file)

# Select only numerical columns
numerical_df = df.select_dtypes(include=["float64", "int64"])

# Compute the correlation matrix for numerical features
correlation_matrix = numerical_df.corr()

# Visualise the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=False, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix")
plt.show()

# Save the correlation matrix to a CSV file for reference
output_csv = "output/correlation_matrix.csv"
correlation_matrix.to_csv(output_csv)
print(f"Correlation analysis completed and saved at: {output_csv}")
