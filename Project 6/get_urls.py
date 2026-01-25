import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

product_info = []

base_url = "https://www.petsmart.com/search/f/category/dry%20food?q=dog%2520food&page={}"

session = requests.Session()
session.headers.update({
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
})

def extract_json_from_html(html):
    soup = BeautifulSoup(html, "lxml")
    for script in soup.find_all("script"):
        text = script.text.strip()
        if text.startswith("{") and "itemListElement" in text:
            return json.loads(text)
    raise Exception("Product JSON not found")

def extract_products(data):
    products = data["mainEntity"]["itemListElement"]
    rows = []
    for p in products:
        item = p["item"]
        rows.append({
            "NAME": item.get("name"),
            "IMAGE": item.get("image"),
            "URL": item.get("offers", {}).get("url")
        })
    return rows

for page in range(1, 22):
    print(f"\nFetching page {page}")

    url = base_url.format(page)
    resp = session.get(url, timeout=20)
    resp.raise_for_status()                   # It automatically throws an error if the HTTP request failed.

    data = extract_json_from_html(resp.text)
    rows = extract_products(data)

    print(f"Extracted {len(rows)} products")

    product_info.extend(rows)

df = pd.DataFrame(product_info)
df.to_excel("pet_food.xlsx", index=False)

print("\nScraping completed successfully!")