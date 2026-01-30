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

    page.goto("https://www.petsmart.com/dog/food/dry-food/blue-buffalo-life-protection-formulaandtrade-adult-dry-dog-food---chicken-and-brown-rice-41846.html", timeout=60000)

    brand_l = page.query_selector('//a[@data-testid="test-pdp-brand"]')
    brand = brand_l.inner_text().strip() if brand_l else 'N/A'

    flavor_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[0]
    flavor = flavor_l.inner_text().strip() if flavor_l else 'N/A'

    size_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[1]
    size = size_l.inner_text().strip() if size_l else 'N/A'
    print(size)

    price_l = page.query_selector('//div[@data-testid="sparky-price"]')
    if price_l:
        price = price_l.inner_text().strip()
    else:
        price_l = page.query_selector('//div[@class="sparky-c-price--sale"]')
        price = price_l.inner_text().strip()
    print(price)

    clk = page.query_selector_all('//label[@class="variant-base__label"]')
    for sixe_btn in clk:
        sixe_btn.click()
        time.sleep(2)

        size_l = page.query_selector_all('//span[@class="variants-fieldset__legend-value"]')[1]
        size = size_l.inner_text().strip() if size_l else 'N/A'
        print(size)
        price_l = page.query_selector('//div[@data-testid="sparky-price"]')
        if price_l:
            price = price_l.inner_text().strip()
        else:
            price_l = page.query_selector('//div[@class="sparky-c-price--sale"]')
            price = price_l.inner_text().strip()
        
        print(price)

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
                    time.sleeo(2)
                    all.click()
            
    #see_more.scroll_into_view_if_needed()
    #time.sleep(2)
    #see_more.click()
    time.sleep(300)
    
    #ps = page.locator("div").locator("p")
    #ingredients = ps.nth(12).inner_text()
    #nutrients = ps.nth(13).inner_text()

    #print(brand)
    #print(flavor)
    #print(ingredients)
    #print(nutrients)

    context.close()
    browser.close()