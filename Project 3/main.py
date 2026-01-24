import nodriver as uc
import time
import pandas as pd

data = []

async def main():

    browser = await uc.start(user_data_dir = "C:/browser_profiles/boodmo", headless=False)
    page = await browser.get("https://boodmo.com/catalog/5109-brake_drum/m330-nissan/")

    time.sleep(30)  

    titles = await page.select_all("span.product-item-tile__title")
    prices = await page.select_all("span.product-item-tile__price__current")
    mrps = await page.select_all("span.product-item-tile__price__mrp--discount")
    discounts = await page.select_all("span.product-item-tile__price__discount")
    brands = await page.select_all("span.product-item-tile__desc__brand")

    max_len = max(len(titles), len(prices), len(mrps), len(discounts), len(brands))

    for i in range(max_len):
        row = {
            "Title": titles[i].text.strip() if i < len(titles) else None,
            "Price": prices[i].text.strip() if i < len(prices) else "N/A",
            "MRP": mrps[i].text.strip() if i < len(mrps) else "N/A",
            "Discount": discounts[i].text.strip() if i < len(discounts) else "N/A",
            "Brand": brands[i].text.strip() if i < len(brands) else None,
        }
        data.append(row)

    browser.stop()

if __name__ == "__main__":
    uc.loop().run_until_complete(main())

pd.DataFrame(data).to_excel("products.xlsx", index=False)
print(f"Data saved successfully")