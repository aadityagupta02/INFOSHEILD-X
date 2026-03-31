import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

print("Original rows:", len(df))

# Remove empty rows
df = df.dropna()

# Keep only valid labels
df = df[df["label"].isin([0,1])]

# Remove very short text
df = df[df["text"].str.len() > 20]

# Remove extremely long text
df = df[df["text"].str.len() < 500]

# Reset index
df = df.reset_index(drop=True)

print("Cleaned rows:", len(df))

# Save cleaned dataset
df.to_csv("dataset_clean.csv", index=False)

print("Clean dataset saved as dataset_clean.csv")