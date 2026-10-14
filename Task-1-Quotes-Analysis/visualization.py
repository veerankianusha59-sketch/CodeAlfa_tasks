import pandas as pd

df = pd.read_csv("/storage/emulated/0/scraped_data.csv")

top_authors = df["Author"].value_counts().head(10)

print("TOP 10 AUTHORS")
print("----------------")
print(top_authors)

top_authors.to_csv("/storage/emulated/0/top_authors.csv")

print()
print("Visualization data saved successfully!")
print("Location: /storage/emulated/0/top_authors.csv")