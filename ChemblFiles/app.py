import streamlit as st
import pandas as pd
import shap
import pickle
import xgboost as xgb
import matplotlib.pyplot as plt
from multiprocessing import Pool
import os
import gc

# Set Streamlit page config
st.set_page_config(page_title="AI-Powered Drug Analysis", layout="wide")

# Chunk size for SHAP computation
CHUNK_SIZE = 500  # Adjust based on memory and dataset size

# Load the XGBoost model saved as a pickle file
@st.cache_resource
def load_model():
    model_path = "output/models/xgboost_final_model.pkl"
    with open(model_path, "rb") as file:
        model = pickle.load(file)  # Use pickle to load the saved model
    return model

# Load validation dataset
@st.cache_data
def load_validation_data():
    X_val_path = "output/features/cleaned/X_val_cleaned.parquet"
    return pd.read_parquet(X_val_path)

# Optimize dataframe to reduce memory usage
def optimize_dataframe(df):
    for col in df.columns:
        if df[col].dtype == 'float64':
            df[col] = df[col].astype('float32')
        elif df[col].dtype == 'int64':
            df[col] = df[col].astype('int32')
    return df

# Align dataset features with model features
def align_features(df, model):
    model_features = model.feature_names if isinstance(model, xgb.Booster) else model.get_booster().feature_names
    missing_features = [feat for feat in model_features if feat not in df.columns]
    for feat in missing_features:
        df[feat] = 0
    return df[model_features]

# Function for multiprocessing SHAP computation
def compute_shap_chunk(chunk, model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    explainer = shap.TreeExplainer(model)
    shap_values_chunk = explainer.shap_values(chunk)

    # Convert numpy array to DataFrame for compatibility
    shap_values_df = pd.DataFrame(
        shap_values_chunk,
        columns=chunk.columns,
        index=chunk.index
    )
    return shap_values_df

# SHAP computation with multiprocessing
def compute_shap_multiprocessing(model, X_val, model_path):
    num_rows = len(X_val)
    chunks = [X_val.iloc[i:i + CHUNK_SIZE] for i in range(0, num_rows, CHUNK_SIZE)]
    output_path = "output/shap_values/"
    os.makedirs(output_path, exist_ok=True)

    with Pool(processes=min(4, os.cpu_count())) as pool:
        for i, result in enumerate(pool.starmap(compute_shap_chunk, [(chunk, model_path) for chunk in chunks])):
            # Save each result to disk
            result.to_parquet(f"{output_path}shap_values_part_{i}.parquet", engine="pyarrow", compression="snappy")
            gc.collect()

    # Merge SHAP values from disk
    shap_values_list = []
    for file in sorted(os.listdir(output_path)):
        shap_values_list.append(pd.read_parquet(os.path.join(output_path, file)))

    # Combine all SHAP values
    shap_values_combined = pd.concat(shap_values_list, axis=0)
    return shap_values_combined

# Plot feature importance
def plot_feature_importance(model):
    st.subheader("Feature Importance")
    fig, ax = plt.subplots(figsize=(10, 6))
    if isinstance(model, xgb.Booster):
        xgb.plot_importance(model, importance_type="weight", ax=ax, max_num_features=20)
    else:
        booster = model.get_booster()
        xgb.plot_importance(booster, importance_type="weight", ax=ax, max_num_features=20)
    st.pyplot(fig)

# Plot SHAP summary
def plot_shap_summary(shap_values, X_val):
    st.subheader("SHAP Summary Plot")
    fig, ax = plt.subplots()
    shap.summary_plot(shap_values.values, X_val, show=False)
    st.pyplot(fig)

# Plot SHAP dependence
def plot_shap_dependence(shap_values, X_val, primary_feature, interaction_feature=None):
    st.subheader(f"SHAP Dependence Plot for {primary_feature}")
    try:
        fig, ax = plt.subplots()
        shap.dependence_plot(
            primary_feature,
            shap_values.values,
            X_val,
            interaction_index=interaction_feature,
            show=False,
            ax=ax
        )
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error generating dependence plot: {e}")

# Main Streamlit App
def main():
    st.title("AI-Powered Drug Analysis Pipeline Dashboard")

    # Load model
    model = load_model()
    model_path = "output/models/xgboost_final_model.pkl"

    # Tabs for navigation
    tab1, tab2, tab3 = st.tabs(["Feature Importance", "SHAP Analysis", "Metrics"])  # Removed "Dataset Upload"

    with tab1:
        plot_feature_importance(model)

    with tab2:
        st.subheader("SHAP Analysis with Background Computation")
        if st.button("Start SHAP Computation"):
            with st.spinner("Computing SHAP values. This may take a while..."):
                X_val = optimize_dataframe(load_validation_data())
                shap_values = compute_shap_multiprocessing(model, X_val, model_path)
                st.session_state["shap_values"] = shap_values
                st.success("SHAP computation completed!")

        if "shap_values" in st.session_state and st.session_state["shap_values"] is not None:
            X_val = optimize_dataframe(load_validation_data())
            plot_shap_summary(st.session_state["shap_values"], X_val)

            valid_features = [col for col in X_val.columns if X_val[col].nunique() > 1 and not X_val[col].isnull().all()]
            if not valid_features:
                st.warning("No valid features available for dependence plot.")
            else:
                primary_feature = st.selectbox("Select Primary Feature for X-Axis", valid_features)
                interaction_feature = st.selectbox(
                    "Select Interaction Feature for Color Bar (Optional)", ["Auto"] + valid_features
                )

                interaction_feature = None if interaction_feature == "Auto" else interaction_feature
                if primary_feature:
                    plot_shap_dependence(
                        st.session_state["shap_values"], X_val, primary_feature, interaction_feature
                    )

    with tab3:
        st.subheader("Model Evaluation Metrics")
        st.write("**RMSE:** 0.1577")
        st.write("**R² Score:** 0.9900")
        st.write("**Training Time:** Approx. 10 seconds")

if __name__ == "__main__":
    main()
