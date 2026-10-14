import pandas as pd
import html

file_path = "/storage/emulated/0/eda_results.csv"
df = pd.read_csv(file_path)

total_quotes = len(df)
total_authors = df["Author"].nunique()
average_length = round(df["Quote_Length"].mean(), 2)
shortest = int(df["Quote_Length"].min())
longest = int(df["Quote_Length"].max())
missing = int(df[["Quote", "Author"]].isnull().sum().sum())

top_authors = df["Author"].value_counts().head(5)

author_rows = ""
for author, count in top_authors.items():
    author_rows += (
        "<tr><td>" + html.escape(str(author)) +
        "</td><td>" + str(count) + "</td></tr>"
    )

length_groups = [
    ("34-60", 34, 60),
    ("61-100", 61, 100),
    ("101-200", 101, 200),
    ("201-500", 201, 500),
    ("501+", 501, float("inf"))
]

length_rows = ""
for label, low, high in length_groups:
    if high == float("inf"):
        count = int((df["Quote_Length"] >= low).sum())
    else:
        count = int(
            ((df["Quote_Length"] >= low) &
             (df["Quote_Length"] <= high)).sum()
        )

    length_rows += (
        "<tr><td>" + label +
        "</td><td>" + str(count) + "</td></tr>"
    )

dashboard = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Quotes EDA Dashboard</title>
<style>
body {
    font-family: Arial, sans-serif;
    background: #f1f5f9;
    color: #1e293b;
    padding: 15px;
}
.container {
    max-width: 800px;
    margin: auto;
}
header {
    background: #1e3a8a;
    color: white;
    padding: 20px;
    text-align: center;
    border-radius: 12px;
}
.cards {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 20px 0;
}
.card {
    flex: 1 1 130px;
    box-sizing: border-box;
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 6px #ddd;
}
.card h3 {
    font-size: 14px;
    color: #64748b;
}
.card p {
    font-size: 24px;
    font-weight: bold;
    color: #2563eb;
    overflow-wrap: anywhere;
}
.section {
    background: white;
    padding: 18px;
    border-radius: 10px;
    margin: 18px 0;
    overflow-x: auto;
}
table {
    width: 100%;
    border-collapse: collapse;
}
th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
th {
    background: #dbeafe;
}
footer {
    text-align: center;
    color: #64748b;
    padding: 15px;
}
</style>
</head>
<body>
<div class="container">
<header>
<h1>Quotes EDA Dashboard</h1>
<p>Exploratory Data Analysis with Python and Pandas</p>
</header>

<div class="cards">
<div class="card">
<h3>Total Quotes</h3>
<p>""" + str(total_quotes) + """</p>
</div>
<div class="card">
<h3>Unique Authors</h3>
<p>""" + str(total_authors) + """</p>
</div>
<div class="card">
<h3>Average Quote Length</h3>
<p>""" + str(average_length) + """</p>
</div>
<div class="card">
<h3>Missing Values</h3>
<p>""" + str(missing) + """</p>
</div>
</div>

<div class="section">
<h2>Top 5 Authors</h2>
<table>
<tr><th>Author</th><th>Number of Quotes</th></tr>
""" + author_rows + """
</table>
</div>

<div class="section">
<h2>Quote Length Distribution</h2>
<table>
<tr><th>Length in Characters</th><th>Number of Quotes</th></tr>
""" + length_rows + """
</table>
</div>

<div class="section">
<h2>Key Findings</h2>
<p>No missing values were found in the original dataset.</p>
<p>Average quote length: """ + str(average_length) + """ characters.</p>
<p>Shortest quote: """ + str(shortest) + """ characters.</p>
<p>Longest quote: """ + str(longest) + """ characters.</p>
<p>Most frequent author: """ + html.escape(str(top_authors.index[0])) + """</p>
<p>Number of duplicate quote-author records: """ + str(int(df.duplicated(subset=["Quote", "Author"]).sum())) + """</p>
<p><b>Recommendation:</b> Review longer quotes separately and use a larger dataset for further analysis.</p>
</div>

<footer>
Dataset: 100 sample quotes | Python, Pandas, HTML and CSS
</footer>
</div>
</body>
</html>
"""

output_path = "/storage/emulated/0/eda_dashboard.html"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(dashboard)

print("EDA dashboard created successfully!")
print("Total quotes:", total_quotes)
print("Unique authors:", total_authors)
print("Dashboard saved to:", output_path)