from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1280, "height":800})
    page = context.new_page()

    page.set_extra_http_headers({
        "Accept-language": "en=US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    })

    page.goto("https://www.petsmart.com/dog/food/dry-food/purina-pro-plan-complete-essentials-shredded-blend-adult-dry-dog-food---chicken-and-rice-3022.html", timeout=60000)

    brand_l = page.query_selector('//a[@data-testid="test-pdp-brand"]')
    brand = brand_l.inner_text().strip() if brand_l else 'N/A'

    flavor_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[0]
    flavor = flavor_l.inner_text().strip() if flavor_l else 'N/A'
 
#   price and size
    for i in range(1,5):
        price_l = page.query_selector('//div[@class="product-price"]')
        price = price_l.inner_text().strip()
        print(price)

        size_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[1]
        size = size_l.inner_text().strip() if size_l else 'N/A'
        print(size)

        next_size = page.query_selector_all('//span[@class="variant-base__label-text"]')[i].click()
        time.sleep(1)

    print(brand)
    print(flavor)

    context.close()
    browser.close()