First Visualisations

This folder contains the initial visualisations created during the Exploratory Data Analysis (EDA) stage of the AI-Powered Drug Analysis Pipeline project. These visualisations focus on understanding the distributions and identifying patterns or anomalies in key variables.

Visualisations

1. STANDARD_VALUE

Original Distribution:

Highly skewed with extreme outliers.

Values span a very large range, making the distribution difficult to interpret.

Filtered Distribution:

After removing extreme outliers (values > 1e6), the distribution is more interpretable but still right-skewed.

Log-Transformed Distribution:

A logarithmic transformation was applied to normalize the distribution.

Resulting distribution is much more symmetric, making it suitable for further analysis.

2. ALOGP

Distribution:

Symmetrical and resembles a normal distribution.

No major issues identified, although a few outliers are present.

Box Plot:

Outliers observed, but these likely represent valid data points.

3. HBA (Hydrogen Bond Acceptors)

Distribution:

Right-skewed with values generally between 0 and 30.

A small number of extreme outliers observed.

Box Plot:

Outliers extend beyond 30, but they are plausible depending on the context.

4. HBD (Hydrogen Bond Donors)

Distribution:

Right-skewed, with most values between 0 and 10.

A small number of extreme outliers.

Box Plot:

Outliers are present but not excessively extreme.

5. MW_FREEBASE (Molecular Weight)

Distribution:

Right-skewed with most values below 1000.

A few extreme outliers extend beyond 5000.

Box Plot:

Outliers are visible but expected for molecular weight data.

Notes

The log-transformed STANDARD_VALUE is the preferred version for further analysis due to its normalized distribution.

These visualisations provide a baseline understanding of the data and help guide decisions in the next stages of the pipeline, such as feature engineering and correlation analysis.

P.S These visualisations were created using Python libraries such as Matplotlib and Seaborn.

The visualisation data originates from processed_data.csv.
