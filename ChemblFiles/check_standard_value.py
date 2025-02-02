import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
file_path = 'output/processed_data.csv'
data = pd.read_csv(file_path)

# Summary statistics for STANDARD_VALUE
print("Summary statistics for STANDARD_VALUE:")
print(data['STANDARD_VALUE'].describe())

# Identify and print outliers
outliers = data[data['STANDARD_VALUE'] > 1e6]
print(f"\nNumber of outliers (STANDARD_VALUE > 1e6): {len(outliers)}")
print(outliers)

# Apply log transformation (replacing zeroes with NaN to avoid errors)
data['STANDARD_VALUE'] = data['STANDARD_VALUE'].replace(0, np.nan)
data['LOG_STANDARD_VALUE'] = np.log10(data['STANDARD_VALUE'])

# Plot log-transformed distribution
print("\nPlotting log-transformed distribution...")
sns.histplot(data['LOG_STANDARD_VALUE'].dropna(), kde=True, bins=50)
plt.title('Log-Transformed Distribution of STANDARD_VALUE')
plt.xlabel('Log10(STANDARD_VALUE)')
plt.ylabel('Frequency')
plt.show()

# Optional: Filter outliers and re-plot original distribution
filtered_data = data[data['STANDARD_VALUE'] < 1e6]
sns.histplot(filtered_data['STANDARD_VALUE'], kde=True, bins=50)
plt.title('Filtered Distribution of STANDARD_VALUE')
plt.xlabel('STANDARD_VALUE')
plt.ylabel('Frequency')
plt.show()
