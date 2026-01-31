from playwright.sync_api import sync_playwright
import time
import pandas as pd

# Reading URLs from excel file
df = pd.read_excel("pet_food.xlsx")
urls = df["URL"].dropna().tolist()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1280, "height":800})
    page = context.new_page()

    page.set_extra_http_headers({
        "Accept-language": "en=US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    })

    for idx, url in enumerate(urls, start=1):
        print(f"[{idx}] Visiting: {url}")
        page.goto(url, timeout=60000)

        brand_l = page.query_selector('//a[@data-testid="test-pdp-brand"]')
        brand = brand_l.inner_text().strip() if brand_l else 'N/A'

        flavor_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[0]
        flavor = flavor_l.inner_text().strip() if flavor_l else 'N/A'

        size_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[1]
        size = size_l.inner_text().strip() if size_l else 'N/A'
        print(f"Size: {size}")

        price_l = page.query_selector('//div[@data-testid="sparky-price"]')
        if price_l:
            price = price_l.inner_text().strip()
        else:
            price_l = page.query_selector('//div[@class="sparky-c-price--sale"]')
            price = price_l.inner_text().strip()
        print(f"Price: {price}")

        clk = page.query_selector_all('//label[@class="variant-base__label"]')
        for sixe_btn in clk:
            sixe_btn.click()
            time.sleep(2)

            size_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[1]
            size = size_l.inner_text().strip() if size_l else 'N/A'
            print(f"Size: {size}")
            price_l = page.query_selector('//div[@data-testid="sparky-price"]')
            if price_l:
                price = price_l.inner_text().strip()
            else:
                price_l = page.query_selector('//div[@class="sparky-c-price--sale"]')
                price = price_l.inner_text().strip()
           
            print(f"Price: {price}")

        ingrd_btns = page.query_selector_all('//a[@class="sparky-c-tabs__link"]')
        for ingrd_btn in ingrd_btns:
            text = ingrd_btn.inner_text().strip()
            if text == "Ingredients":
                time.sleep(2)
                ingrd_btn.click()
                see_more = page.query_selector_all('//span[@class="sparky-c-button__text"]')
                for all in see_more:
                    inr_txt = all.inner_text().strip()
                    if inr_txt == "See more":
                        time.sleep(2)
                        all.click()
                        items = page.query_selector('//div[@class="sparky-c-text-passage__inner"]')
                        item = items.inner_text().strip()
                        print(f"Ingredients/Nutrients: {item}")
                        #Using regex i can get ingredients list and guarenteed analysis from here
            else:
                print("Can't find nutients")
        time.sleep(300)

        print(f"Brand: {brand}")
        print(f"Flavor: {flavor}")

    context.close()
    browser.close()
