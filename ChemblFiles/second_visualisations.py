import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load the cleaned data
file_path = 'output/cleaned_data.csv'
data = pd.read_csv(file_path)

# Define columns to plot
columns_to_plot = ['STANDARD_VALUE', 'LOG_STANDARD_VALUE', 'ALOGP', 'HBA', 'HBD', 'MW_FREEBASE']

# Output directory for saving plots
output_dir = 'plot diagrams/Second Visualisations/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Generate and save histograms
for column in columns_to_plot:
    sns.histplot(data[column].dropna(), kde=True, bins=50)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(f'{output_dir}{column}_distribution.png')
    plt.close()

# Generate and save box plots
for column in columns_to_plot:
    sns.boxplot(x=data[column].dropna())
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.savefig(f'{output_dir}{column}_boxplot.png')
    plt.close()

print("Second set of visualisations generated and saved.")