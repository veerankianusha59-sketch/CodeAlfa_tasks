import pandas as pd

# Load the quotes dataset
file_path = "/storage/emulated/0/scraped_data.csv"
df = pd.read_csv(file_path)

print("=" * 40)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 40)

# 1. Dataset information
print("\n1. DATASET INFORMATION")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("Column names:", list(df.columns))

# 2. Check missing values
print("\n2. MISSING VALUES")
print(df.isnull().sum())

# 3. Check duplicate records
print("\n3. DUPLICATE RECORDS")
print("Duplicates:", df.duplicated().sum())

# 4. Analyze quote lengths
df["Quote_Length"] = df["Quote"].astype(str).str.len()

print("\n4. QUOTE LENGTH ANALYSIS")
print("Average length:", round(df["Quote_Length"].mean(), 2))
print("Shortest quote:", df["Quote_Length"].min())
print("Longest quote:", df["Quote_Length"].max())

# 5. Most frequent authors
print("\n5. TOP 5 AUTHORS")
print(df["Author"].value_counts().head(5))

# 6. Summary statistics
print("\n6. SUMMARY STATISTICS")
print(df["Quote_Length"].describe())

# 7. Save analyzed dataset
output_path = "/storage/emulated/0/eda_results.csv"
df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully!")
print("Results saved to:", output_path)