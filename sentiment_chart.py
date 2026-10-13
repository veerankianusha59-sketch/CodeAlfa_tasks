import pandas as pd

# Load sentiment analysis results
file_path = "/storage/emulated/0/quotes_sentiment_analysis.csv"
df = pd.read_csv(file_path)

# Count sentiments
counts = df["Sentiment"].value_counts()

positive = int(counts.get("Positive", 0))
neutral = int(counts.get("Neutral", 0))
negative = int(counts.get("Negative", 0))

# Create an HTML chart
html = f"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quotes Sentiment Analysis</title>

<style>
body {{
    font-family: Arial, sans-serif;
    background: #f2f5fa;
    padding: 20px;
    text-align: center;
}}

.card {{
    background: white;
    padding: 20px;
    border-radius: 15px;
    max-width: 500px;
    margin: auto;
    box-shadow: 0 4px 12px #cccccc;
}}

.bar-container {{
    text-align: left;
    margin: 20px 0;
}}

.bar {{
    color: white;
    padding: 10px;
    border-radius: 6px;
    min-width: 35px;
    box-sizing: border-box;
}}

.positive {{ background: #28a745; }}
.neutral {{ background: #e0a800; }}
.negative {{ background: #dc3545; }}

p {{ font-size: 16px; }}
</style>
</head>

<body>
<div class="card">
<h1>Quotes Sentiment Analysis</h1>
<p>Total Quotes: {len(df)}</p>

<div class="bar-container">
<b>Positive: {positive}</b>
<div class="bar positive" style="width:{positive}%">
{positive}%
</div>
</div>

<div class="bar-container">
<b>Neutral: {neutral}</b>
<div class="bar neutral" style="width:{neutral}%">
{neutral}%
</div>
</div>

<div class="bar-container">
<b>Negative: {negative}</b>
<div class="bar negative" style="width:{negative}%">
{negative}%
</div>
</div>

<p>Positive quotes are the largest category in this dataset.</p>
</div>
</body>
</html>
"""

output_path = "/storage/emulated/0/sentiment_chart.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(html)

print("Sentiment chart created successfully!")
print("Positive:", positive)
print("Neutral:", neutral)
print("Negative:", negative)
print("Saved to:", output_path)