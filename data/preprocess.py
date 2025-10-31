import os
import pandas as pd

raw_folder = 'data/raw'

files = [f for f in os.listdir(raw_folder) if f.endswith('.csv')]
print("Files found in raw folder:", files)

all_dataframes = []
for fname in files:
    path = os.path.join(raw_folder, fname)
    print(f"Loading {fname} ...")
    try:
        df = pd.read_csv(path)
        all_dataframes.append(df)
        print(f"Loaded {fname}.")
    except Exception as e:
        print(f"Failed to load {fname}: {e}")

if all_dataframes:
    full_df = pd.concat(all_dataframes, ignore_index=True)
    os.makedirs('data/processed', exist_ok=True)
    full_df.to_csv('data/processed/cic_ids_full.csv', index=False)
    print("Saved combined file to data/processed/cic_ids_full.csv")
else:
    print("No data loaded. Please check your files.")