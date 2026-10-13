import pandas as pd
from textblob import TextBlob

# Load the quotes dataset
file_path = "/storage/emulated/0/scraped_data.csv"
df = pd.read_csv(file_path)

# Analyze sentiment
def analyze_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return polarity, sentiment

# Apply sentiment analysis
df["Polarity"], df["Sentiment"] = zip(
    *df["Quote"].apply(analyze_sentiment)
)

# Display results
print("QUOTES SENTIMENT ANALYSIS")
print("=========================")
print("\nTotal Quotes:", len(df))

print("\nSentiment Counts:")
print(df["Sentiment"].value_counts())

print("\nSample Results:")
print(df[["Quote", "Polarity", "Sentiment"]].head(10))

# Save the results
output_path = "/storage/emulated/0/quotes_sentiment_analysis.csv"
df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully!")
print("Results saved to:", output_path)