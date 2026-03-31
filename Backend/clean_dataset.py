import pandas as pd

df = pd.read_csv("dataset.csv")

print("Original rows:", len(df))

# Convert labels to numbers safely
df["label"] = pd.to_numeric(df["label"], errors="coerce")

# Remove rows with invalid labels
df = df.dropna(subset=["label"])

# Keep only 0 or 1
df = df[df["label"].isin([0,1])]

# Remove empty text
df = df.dropna(subset=["text"])

# Remove very short text
df = df[df["text"].str.len() > 20]

# Remove extremely long text
df = df[df["text"].str.len() < 500]

df = df.reset_index(drop=True)

print("Cleaned rows:", len(df))

df.to_csv("dataset_clean.csv", index=False)

print("Clean dataset saved.")