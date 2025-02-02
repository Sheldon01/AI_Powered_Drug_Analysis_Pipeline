import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed data
file_path = 'output/processed_data.csv'
data = pd.read_csv(file_path)

# Columns to visualise
columns_to_plot = ['STANDARD_VALUE', 'MW_FREEBASE', 'ALOGP', 'HBA', 'HBD']

# Plot histograms
for column in columns_to_plot:
    sns.histplot(data[column], kde=True, bins=50)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Example: Box plot for outliers
for column in columns_to_plot:
    sns.boxplot(x=data[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()
