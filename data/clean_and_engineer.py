import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data():
    path = 'data/processed/cic_ids_full.csv'
    print(f"Loading combined data from {path} ...")
    df = pd.read_csv(path)
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

def clean_data(df):
    print("Cleaning data...")
    # Drop duplicate rows
    df = df.drop_duplicates()
    # Drop rows with any missing values
    df = df.dropna()
    print(f"Data shape after cleaning: {df.shape}")
    return df

def select_and_scale_features(df):
    print("Selecting and scaling features...")

    # Strip spaces from column names to avoid mismatch
    df.columns = df.columns.str.strip()

    feature_cols = [
        'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets',
        'Total Length of Fwd Packets', 'Total Length of Bwd Packets',
        'Fwd Packet Length Max', 'Bwd Packet Length Max', 'Flow Bytes/s'
    ]

    for col in feature_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected feature column: {col}")

    features = df[feature_cols]

    # Replace inf/-inf with NaN
    features = features.replace([float('inf'), float('-inf')], pd.NA)

    # Drop rows with NaN
    features = features.dropna()

    print(f"Data shape after removing infinite and NaN values: {features.shape}")

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    df_scaled = pd.DataFrame(scaled_features, columns=feature_cols)

    # Add Label back if exists in original df
    if 'Label' in df.columns:
        # Align labels to features indices after dropna
        df_scaled['Label'] = df.loc[features.index, 'Label'].values

    print("Feature scaling completed.")
    return df_scaled

def save_clean_data(df):
    out_path = 'data/processed/cic_ids_cleaned.csv'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    df.to_csv(out_path, index=False)
    print(f"Cleaned data saved to {out_path}")

def main():
    df = load_data()
    df_clean = clean_data(df)
    df_scaled = select_and_scale_features(df_clean)
    save_clean_data(df_scaled)

if __name__ == "__main__":
    main()