import pandas as pd

df = pd.read_csv("/storage/emulated/0/scraped_data.csv")

print("Dataset loaded successfully!")
print(df.head())

print()
print("Number of rows and columns:")
print(df.shape)

print()
print("Column names:")
print(df.columns)

print()
print("Missing values:")
print(df.isnull().sum())

print()
print("Quotes by each author:")
print(df["Author"].value_counts())

print()
print("Top 5 authors:")
print(df["Author"].value_counts().head(5))

print()
print("Number of unique authors:")
print(df["Author"].nunique())

print()
print("Duplicate rows:")
print(df.duplicated().sum())

print()
print("Dataset information:")
df.info()
print()
print("Quote lengths:")

df["Quote_Length"] = df["Quote"].str.len()

print(df[["Quote", "Quote_Length"]].head())
print()
print("Average quote length:")
print(df["Quote_Length"].mean())
print()
print("Longest quote length:")
print(df["Quote_Length"].max())

print()
print("Shortest quote length:")
print(df["Quote_Length"].min())
print()
print("Average quote length by author:")
print(df.groupby("Author")["Quote_Length"].mean().sort_values(ascending=False).head(5))
from collections import Counter
import re

text = " ".join(df["Quote"])

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

word_counts = Counter(words)

print()
print("Top 10 most common words:")
print(word_counts.most_common(10))
stop_words = {
    "the", "is", "a", "it", "to", "of", "and", "you",
    "i", "in", "that", "for", "my", "on", "with", "be",
    "as", "are", "this", "your", "not", "but", "have",
    "we", "he", "his", "her", "they", "was", "our"
}

meaningful_words = [word for word in words if word not in stop_words]

meaningful_counts = Counter(meaningful_words)

print()
print("Top 10 meaningful words:")
print(meaningful_counts.most_common(10))
meaningful_words = [
    word for word in words
    if word not in stop_words and len(word) > 2
]

meaningful_counts = Counter(meaningful_words)

print()
print("Top 10 cleaned meaningful words:")
print(meaningful_counts.most_common(10))
print()
print("===== EDA SUMMARY =====")

print("Total quotes:", len(df))
print("Total authors:", df["Author"].nunique())
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print("Average quote length:", round(df["Quote_Length"].mean(), 2))
print("Longest quote:", df["Quote_Length"].max())
print("Shortest quote:", df["Quote_Length"].min())

print()
print("Most common author:")
print(df["Author"].value_counts().head(1))

print()
print("Most common meaningful word:")
print(meaningful_counts.most_common(1))
print()
print("Top 10 authors for visualization:")

top_10_authors = df["Author"].value_counts().head(10)

print(top_10_authors)
# ==========================================
# VISUALIZATION 2: AVERAGE QUOTE LENGTH
# ==========================================

print("\nAVERAGE QUOTE LENGTH BY AUTHOR")
print("--------------------------------")

# Calculate average quote length for each author
avg_length = df.groupby("Author")["Quote_Length"].mean()

# Select top 10 authors by average quote length
top_avg_length = avg_length.sort_values(ascending=False).head(10)

print(top_avg_length)

# Create HTML chart
html = """
<!DOCTYPE html>
<html>
<head>
<title>Average Quote Length by Author</title>

<style>
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h2 {
    text-align: center;
}

.bar-container {
    margin: 12px 0;
}

.author {
    font-size: 14px;
    margin-bottom: 4px;
}

.bar {
    background-color: #4CAF50;
    color: white;
    padding: 6px;
    text-align: right;
    box-sizing: border-box;
}

</style>
</head>

<body>

<h2>Top 10 Authors by Average Quote Length</h2>
"""

max_value = top_avg_length.max()

for author, value in top_avg_length.items():

    width = (value / max_value) * 100

    html += f"""
    <div class="bar-container">
        <div class="author">{author}</div>
        <div class="bar" style="width:{width}%">
            {value:.2f}
        </div>
    </div>
    """

html += """
</body>
</html>
"""

# Save HTML file
file_path = "/storage/emulated/0/average_quote_length.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nAVERAGE QUOTE LENGTH CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# ==========================================
# TOP 10 CLEANED MEANINGFUL WORDS
# ==========================================

print("\nTOP 10 MOST MEANINGFUL WORDS")
print("-----------------------------")

# Use the meaningful words already calculated in your program
top_words = [
    ('love', 23),
    ('can', 21),
    ('who', 18),
    ('will', 18),
    ('what', 17),
    ('one', 15),
    ('all', 15),
    ('never', 13),
    ('she', 13),
    ('life', 12)
]

print(top_words)

# Create HTML bar chart
html = """
<html>
<head>
<title>Top 10 Meaningful Words</title>
<style>
body {
    font-family: Arial;
    margin: 20px;
}
h2 {
    text-align: center;
}
.bar-container {
    margin: 12px 0;
}
.label {
    font-size: 14px;
    margin-bottom: 3px;
}
.bar {
    height: 30px;
    background-color: #2196F3;
    color: white;
    text-align: right;
    padding-right: 8px;
    line-height: 30px;
    box-sizing: border-box;
}
</style>
</head>

<body>

<h2>Top 10 Most Meaningful Words</h2>
"""

max_count = top_words[0][1]

for word, count in top_words:
    width = (count / max_count) * 100

    html += f"""
    <div class="bar-container">
        <div class="label">{word}</div>
        <div class="bar" style="width:{width}%;">
            {count}
        </div>
    </div>
    """

html += """
</body>
</html>
"""

file_path = "/storage/emulated/0/top_meaningful_words.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nMEANINGFUL WORDS CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# ==========================================
# QUOTE LENGTH DISTRIBUTION
# ==========================================

print("\nQUOTE LENGTH DISTRIBUTION")
print("--------------------------")

# Create length groups
bins = [0, 50, 100, 150, 200, 300, 500, 1000, 2000]
labels = [
    "0-50",
    "51-100",
    "101-150",
    "151-200",
    "201-300",
    "301-500",
    "501-1000",
    "1001+"
]

df["Length_Group"] = pd.cut(
    df["Quote_Length"],
    bins=bins,
    labels=labels,
    include_lowest=True
)

length_counts = df["Length_Group"].value_counts().sort_index()

print(length_counts)

# Create HTML bar chart
html = """
<html>
<head>
<title>Quote Length Distribution</title>

<style>
body {
    font-family: Arial;
    margin: 20px;
}

h2 {
    text-align: center;
}

.bar-container {
    margin: 15px 0;
}

.label {
    font-size: 14px;
    margin-bottom: 4px;
}

.bar {
    height: 30px;
    background-color: #2196F3;
    color: white;
    text-align: right;
    padding-right: 8px;
    line-height: 30px;
    box-sizing: border-box;
}
</style>

</head>

<body>

<h2>Quote Length Distribution</h2>
"""

max_count = length_counts.max()

for label, count in length_counts.items():

    width = (count / max_count) * 100

    html += f"""
    <div class="bar-container">
        <div class="label">{label} characters</div>

        <div class="bar" style="width:{width}%;">
            {count}
        </div>
    </div>
    """

html += """
</body>
</html>
"""

file_path = "/storage/emulated/0/quote_length_distribution.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nQUOTE LENGTH DISTRIBUTION CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# TOP 10 MOST COMMON WORDS
from collections import Counter
import re

print("\nTOP 10 MOST COMMON WORDS")
print("-------------------------")

all_words = []

for quote in df["Quote"]:
    words = re.findall(r"\b[a-zA-Z]+\b", quote.lower())
    all_words.extend(words)

word_counts = Counter(all_words)

top_common_words = word_counts.most_common(10)

print(top_common_words)

# Create HTML chart
labels = [item[0] for item in top_common_words]
values = [item[1] for item in top_common_words]

html = """
<!DOCTYPE html>
<html>
<head>
<title>Top 10 Most Common Words</title>
<style>
body {
    font-family: Arial;
    margin: 20px;
}
h2 {
    text-align: center;
}
.bar {
    height: 25px;
    background: #2196F3;
    margin: 10px 0;
    color: white;
    text-align: right;
    padding-right: 5px;
}
</style>
</head>
<body>

<h2>Top 10 Most Common Words</h2>
"""

max_value = max(values)

for word, count in top_common_words:
    width = (count / max_value) * 100
    html += f"""
    <p>{word}</p>
    <div class="bar" style="width:{width}%">
        {count}
    </div>
    """

html += """
</body>
</html>
"""

file_path = "/storage/emulated/0/top_common_words.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nTOP COMMON WORDS CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# TOP AUTHORS BY AVERAGE QUOTE LENGTH

print("\nTOP AUTHORS BY AVERAGE QUOTE LENGTH")
print("-----------------------------------")

avg_length = df.groupby("Author")["Quote_Length"].mean()
top_avg_length = avg_length.sort_values(ascending=False).head(10)

print(top_avg_length)

labels = top_avg_length.index.tolist()
values = top_avg_length.values.tolist()

html = """
<!DOCTYPE html>
<html>
<head>
<title>Top Authors by Average Quote Length</title>
<style>
body {
    font-family: Arial;
    margin: 20px;
}
h2 {
    text-align: center;
}
.bar {
    height: 30px;
    background: #673AB7;
    margin: 12px 0;
    color: white;
    text-align: right;
    padding-right: 8px;
    line-height: 30px;
}
</style>
</head>
<body>

<h2>Top Authors by Average Quote Length</h2>
"""

max_value = max(values)

for author, value in zip(labels, values):
    width = (value / max_value) * 100
    html += f"""
    <p>{author}</p>
    <div class="bar" style="width:{width}%">
        {value:.2f}
    </div>
    """

html += """
</body>
</html>
"""

file_path = "/storage/emulated/0/top_authors_average_length.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nTOP AUTHORS AVERAGE LENGTH CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# TOP 5 AUTHORS PIE CHART

print("\nTOP 5 AUTHORS PIE CHART")
print("-----------------------")

top5 = df["Author"].value_counts().head(5)

print(top5)

labels = top5.index.tolist()
values = top5.values.tolist()

colors = [
    "#4CAF50",
    "#2196F3",
    "#FF9800",
    "#9C27B0",
    "#F44336"
]

html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Top 5 Authors</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

</head>

<body>

<h2 style="text-align:center;">
Top 5 Authors by Number of Quotes
</h2>

<canvas id="myChart"></canvas>

<script>

const ctx = document.getElementById('myChart');

new Chart(ctx, {{
    type: 'pie',

    data: {{
        labels: {labels},

        datasets: [{{
            data: {values},
            backgroundColor: {colors}
        }}]
    }},

    options: {{
        responsive: true
    }}
}});

</script>

</body>
</html>
"""

file_path = "/storage/emulated/0/top5_authors_pie.html"

with open(file_path, "w", encoding="utf-8") as file:
    file.write(html)

print("\nTOP 5 AUTHORS PIE CHART CREATED SUCCESSFULLY!")
print("Location:", file_path)
# EDA INSIGHTS

print("\n===== EDA INSIGHTS =====")

print("1. The dataset contains 100 quotes from 50 different authors.")
print("2. There are no missing values in the dataset.")
print("3. There are no duplicate rows.")
print("4. Albert Einstein has the highest number of quotes with 10.")
print("5. The average quote length is 122.27 characters.")
print("6. The longest quote contains 1084 characters.")
print("7. The shortest quote contains 34 characters.")
print("8. Pablo Neruda has the highest average quote length at 319 characters.")
print("9. 'love' is the most common meaningful word with 23 occurrences.")
print("10. Most quotes belong to the 51-100 character length group.")

print("\n===== EDA COMPLETED SUCCESSFULLY =====")