import pandas as pd

df = pd.read_csv('data/processed/cic_ids_full.csv')
print("Columns in dataset:")
print(df.columns.tolist())
