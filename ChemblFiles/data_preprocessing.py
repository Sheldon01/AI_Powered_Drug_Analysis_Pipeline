import os
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors

# File paths
DATA_DIR = 'data/'
OUTPUT_DIR = 'output/'

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to load, clean, and validate datasets
def load_and_clean_csv(file_path, expected_columns):
    try:
        # Load file while skipping problematic lines
        data = pd.read_csv(file_path, header=None, on_bad_lines='skip', engine='python')
        print(f"Loaded {file_path} with {data.shape[0]} rows.")

        # Assign headers to the dataframe
        data.columns = expected_columns

        # Check for missing critical columns
        missing_cols = [col for col in expected_columns if col not in data.columns]
        if missing_cols:
            print(f"WARNING: Missing columns {missing_cols} in {file_path}.")

        return data
    except Exception as e:
        print(f"ERROR: Could not load {file_path}: {e}")
        return pd.DataFrame()

# Load datasets
compound_columns = [
    "MOLREGNO", "PREF_NAME", "THERAPEUTIC_FLAG", "BLACK_BOX_WARNING", "WITHDRAWN_FLAG",
    "CANONICAL_SMILES", "MW_FREEBASE", "ALOGP", "HBA", "HBD", "NUM_RO5_VIOLATIONS"
]
activity_columns = [
    "ACTIVITY_ID", "MOLREGNO", "STANDARD_VALUE", "STANDARD_TYPE", "STANDARD_UNITS", "POTENTIAL_DUPLICATE"
]
mechanism_columns = ["MOLREGNO", "MECHANISM_OF_ACTION", "ACTION_TYPE"]
warning_columns = ["MOLREGNO", "WARNING_TYPE", "WARNING_CLASS", "WARNING_YEAR"]

compound_data = load_and_clean_csv(os.path.join(DATA_DIR, 'compound_data.csv'), compound_columns)
activity_data = load_and_clean_csv(os.path.join(DATA_DIR, 'activity_data.csv'), activity_columns)
mechanism_data = load_and_clean_csv(os.path.join(DATA_DIR, 'mechanism_data.csv'), mechanism_columns)
warning_data = load_and_clean_csv(os.path.join(DATA_DIR, 'warning_data.csv'), warning_columns)

# Process compound_data if valid
if not compound_data.empty and 'CANONICAL_SMILES' in compound_data.columns:
    def compute_descriptors(smiles):
        mol = Chem.MolFromSmiles(smiles)
        if mol:
            return pd.Series([Descriptors.MolWt(mol), Descriptors.MolLogP(mol)])
        else:
            return pd.Series([None, None])

    compound_data[['Molecular_Weight', 'LogP']] = compound_data['CANONICAL_SMILES'].apply(compute_descriptors)
else:
    print("Skipping descriptor computation due to missing CANONICAL_SMILES column.")

# Merge data if all datasets are valid
if not compound_data.empty and not activity_data.empty:
    data_merged = pd.merge(compound_data, activity_data, on='MOLREGNO', how='inner')
    if not mechanism_data.empty:
        data_merged = pd.merge(data_merged, mechanism_data, on='MOLREGNO', how='left')
    if not warning_data.empty:
        data_merged = pd.merge(data_merged, warning_data, on='MOLREGNO', how='left')

    # Save merged data
    output_path = os.path.join(OUTPUT_DIR, 'preprocessed_data.csv')
    data_merged.to_csv(output_path, index=False)
    print(f"Merged data saved to {output_path}.")
else:
    print("ERROR: Merging skipped due to incomplete datasets.")
