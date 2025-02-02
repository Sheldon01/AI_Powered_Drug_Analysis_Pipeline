Second Visualisations

This folder contains the visualisations generated during the exploratory data analysis (EDA) stage of the AI-Powered Drug Analysis Pipeline project. These visualisations focus on understanding the distributions, patterns, and outliers in key molecular properties and bioactivity data.

Visualisations

Log-Transformed

Folder: LogTransformed

Contains visualisations of the log-transformed version of STANDARD_VALUE, named LOG_STANDARD_VALUE.

This version normalises the distribution of STANDARD_VALUE, making it suitable for further analysis.

Individual Visualisations

ALOGP

Box Plot: ALOGP_boxplot.png

Highlights the distribution of ALOGP values and identifies outliers.

Histogram: ALOGP_distribution.png

Displays the frequency distribution of ALOGP values, showing a near-normal distribution.

HBA (Hydrogen Bond Acceptors)

Box Plot: HBA_boxplot.png

Shows the spread of HBA values and indicates outliers above 10.

Histogram: HBA_distribution.png

Right-skewed distribution with most values between 0 and 10.

HBD (Hydrogen Bond Donors)

Box Plot: HBD_boxplot.png

Highlights the distribution and outliers of HBD values, mostly concentrated below 5.

Histogram: HBD_distribution.png

Right-skewed distribution, similar to HBA.

MW_FREEBASE (Molecular Weight)

Box Plot: MW_FREEBASE_boxplot.png

Indicates a central distribution around 400 with minimal outliers.

Histogram: MW_FREEBASE_distribution.png

Shows a near-normal distribution of molecular weights.

STANDARD_VALUE (Original)

Box Plot: STANDARD_VALUE_boxplot.png

Highlights extreme outliers, making this version unsuitable for analysis.

Histogram: STANDARD_VALUE_distribution.png

Highly skewed distribution, with values extending as high as 1e28.

Key Notes

Usable Data:

The log-transformed LOG_STANDARD_VALUE is the preferred version for modelling and analysis.

Variables like ALOGP, HBA, HBD, and MW_FREEBASE are valid and ready for use in correlation or machine learning tasks.

Unusable Data:

The original STANDARD_VALUE visualisations are kept for reference only and will not be used in further analysis due to extreme skewness.

Next Steps

Correlation Analysis:

Assess relationships between LOG_STANDARD_VALUE and other molecular properties.

Feature Selection:

Use the visualisations and correlation results to identify key features for machine learning.

Contact

For any queries, refer to the project documentation or contact the project maintainer.

PS. The visualisations are generated using Python and its libraries like Matplotlib and Seaborn.

The file used for the visualisations is cleaned_data.csv.
