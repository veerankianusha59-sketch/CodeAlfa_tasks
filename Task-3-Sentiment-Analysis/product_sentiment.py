import pandas as pd
from textblob import TextBlob

# Load product reviews
file_path = "/storage/emulated/0/product_reviews.csv"
df = pd.read_csv(file_path)

# Function to analyze sentiment
def analyze_sentiment(review):
    polarity = TextBlob(str(review)).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return polarity, sentiment

# Apply sentiment analysis
df["Polarity"], df["Sentiment"] = zip(
    *df["Review"].apply(analyze_sentiment)
)

# Display results
print("PRODUCT REVIEW SENTIMENT ANALYSIS")
print("=" * 40)
print(df[["Product", "Review", "Polarity", "Sentiment"]])

# Count sentiments
print("\nSENTIMENT COUNTS")
print(df["Sentiment"].value_counts())

# Calculate percentages
print("\nSENTIMENT PERCENTAGES")
print((df["Sentiment"].value_counts(normalize=True) * 100).round(2))

# Save results
output_path = "/storage/emulated/0/product_sentiment_results.csv"
# Product-wise sentiment analysis
print("\nPRODUCT-WISE SENTIMENT ANALYSIS")
print("=" * 40)

product_sentiments = pd.crosstab(
    df["Product"],
    df["Sentiment"]
)

print(product_sentiments)

print("\nPOSITIVE REVIEWS BY PRODUCT")
positive_counts = (
    df[df["Sentiment"] == "Positive"]
    .groupby("Product")
    .size()
)

print(positive_counts)

# Save results
df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully!")
df.to_csv(output_path, index=False)

print("\nAnalysis completed successfully!")
print("Results saved to:", output_path)
# Create an HTML sentiment chart

import html

sentiment_counts = df["Sentiment"].value_counts()

total = len(df)

positive = sentiment_counts.get("Positive", 0)
negative = sentiment_counts.get("Negative", 0)
neutral = sentiment_counts.get("Neutral", 0)

def make_bar(label, count, color):
    percentage = count / total * 100

    return f"""
    <div class="item">
        <p>{label}: {count} reviews ({percentage:.2f}%)</p>
        <div class="bar">
            <div style="width:{percentage}%; background:{color};">
            </div>
        </div>
    </div>
    """

chart = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Product Sentiment Analysis</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f2f5fa;
    padding: 20px;
}}
.card {{
    background: white;
    padding: 20px;
    border-radius: 15px;
    max-width: 600px;
    margin: auto;
    box-shadow: 0 3px 12px #cccccc;
}}
h1 {{
    text-align: center;
    color: #243b64;
}}
.item {{
    margin: 22px 0;
}}
.bar {{
    background: #e5e7eb;
    height: 24px;
    border-radius: 12px;
    overflow: hidden;
}}
.bar div {{
    height: 24px;
    border-radius: 12px;
}}
.note {{
    color: #555;
    font-size: 13px;
}}
</style>
</head>

<body>
<div class="card">
<h1>Product Review Sentiment</h1>
<p>Total reviews analyzed: {total}</p>

{make_bar("Positive 😊", positive, "#22a06b")}
{make_bar("Negative 😞", negative, "#e5484d")}
{make_bar("Neutral 😐", neutral, "#e5a000")}

<h3>Conclusion</h3>
<p>Most reviews in this sample were classified as positive.</p>

<p class="note">
These are sample reviews created for educational purposes,
not real customer feedback. Sentiment labels are estimates.
</p>
</div>
</body>
</html>
"""

chart_path = "/storage/emulated/0/product_sentiment_chart.html"

with open(chart_path, "w", encoding="utf-8") as file:
    file.write(chart)

print("Sentiment chart created successfully!")
print("Chart saved to:", chart_path)
# EMOTION ANALYSIS

def detect_emotion(review):
    text = str(review).lower()

    if any(word in text for word in ["love", "happy", "excellent", "fantastic", "amazing"]):
        return "Happiness"

    elif any(word in text for word in ["terrible", "hate", "angry", "awful"]):
        return "Anger"

    elif any(word in text for word in ["sad", "disappointed", "unhappy"]):
        return "Sadness"

    elif any(word in text for word in ["poor", "slow", "uncomfortable"]):
        return "Dissatisfaction"

    else:
        return "No clear emotion"

# Apply emotion detection
df["Emotion"] = df["Review"].apply(detect_emotion)

print("\nEMOTION ANALYSIS RESULTS")
print("========================")
print(df[["Product", "Review", "Emotion"]])

# Count emotions
print("\nEMOTION COUNTS")
print(df["Emotion"].value_counts())

# Save emotion analysis
emotion_path = "/storage/emulated/0/product_emotion_results.csv"
df.to_csv(emotion_path, index=False)

print("\nEmotion analysis completed!")
print("Results saved to:", emotion_path)
# BUSINESS INSIGHTS REPORT

print("\n" + "=" * 40)
print("BUSINESS INSIGHTS REPORT")
print("=" * 40)

total_reviews = len(df)

positive_count = (df["Sentiment"] == "Positive").sum()
negative_count = (df["Sentiment"] == "Negative").sum()
neutral_count = (df["Sentiment"] == "Neutral").sum()

print("\n1. TOTAL REVIEWS:", total_reviews)

print("\n2. SENTIMENT SUMMARY")
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Neutral:", neutral_count)

print("\n3. POSITIVE REVIEW PERCENTAGE:",
      round(positive_count / total_reviews * 100, 2), "%")

print("\n4. PRODUCT WITH MOST POSITIVE REVIEWS")

positive_by_product = (
    df[df["Sentiment"] == "Positive"]
    .groupby("Product")
    .size()
)

if not positive_by_product.empty:
    highest = positive_by_product.max()
    top_products = positive_by_product[
        positive_by_product == highest
    ].index.tolist()

    print(", ".join(top_products))
    print("Positive reviews:", highest)

print("\n5. MOST DETECTED EMOTION")

emotion_counts = df["Emotion"].value_counts()
print(emotion_counts.idxmax())
print("Number of reviews:", emotion_counts.max())

print("\n6. BUSINESS RECOMMENDATIONS")

if negative_count > 0:
    print("- Review negative feedback to identify product issues.")

if positive_count > 0:
    print("- Identify features customers appreciate.")

print("- Collect more real customer reviews.")
print("- Validate automated sentiment and emotion labels.")
print("- Use larger datasets before making business decisions.")

print("\nNote: Results are based on 11 sample reviews.")
print("They do not represent actual customer opinions.")
print("\nBusiness insights generated successfully!")
# SAVE BUSINESS INSIGHTS REPORT

report_path = "/storage/emulated/0/business_insights_report.txt"

with open(report_path, "w", encoding="utf-8") as file:
    file.write("PRODUCT REVIEW SENTIMENT ANALYSIS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total Reviews: {total_reviews}\n")
    file.write(f"Positive Reviews: {positive_count}\n")
    file.write(f"Negative Reviews: {negative_count}\n")
    file.write(f"Neutral Reviews: {neutral_count}\n")

    positive_percentage = positive_count / total_reviews * 100
    file.write(
        f"Positive Percentage: {positive_percentage:.2f}%\n\n"
    )

    file.write("Product with the most positive reviews:\n")
    file.write(", ".join(top_products) + "\n\n")

    file.write("Most detected emotion:\n")
    file.write(f"{emotion_counts.idxmax()}\n\n")

    file.write("Business Recommendations:\n")
    file.write("- Review negative feedback.\n")
    file.write("- Identify features customers appreciate.\n")
    file.write("- Collect more real customer reviews.\n")
    file.write("- Validate automated predictions.\n")
    file.write("- Use larger datasets for reliable insights.\n\n")

    file.write(
        "Note: Results are based on 11 sample reviews, "
        "not actual customer feedback.\n"
    )

print("Business report saved successfully!")
print("Report location:", report_path)