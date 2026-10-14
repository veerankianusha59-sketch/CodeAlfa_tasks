import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

# Scrape 10 pages
for page in range(1, 11):

    url = f"https://quotes.toscrape.com/page/{page}/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for item in quotes:
        quote = item.find("span", class_="text").text
        author = item.find("small", class_="author").text

        data.append({
            "Quote": quote,
            "Author": author
        })

    print("Page", page, "scraped successfully!")

# Create dataset
df = pd.DataFrame(data)

# Save CSV
df.to_csv("scraped_data.csv", index=False)

print()
print("Total quotes scraped:", len(df))
print("Dataset saved successfully!")