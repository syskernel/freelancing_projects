from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import mouse_movement
import time
from datetime import datetime
import logging
import pandas as pd

products = []

today = datetime.now().strftime("%d-%m-%y")
log_filename = f"logs_{today}.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,  # options: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.getLogger().addHandler(logging.StreamHandler())

def get_data():
    logging.info(f"Saving data from Page {i}")
    items = page.query_selector_all('//div[@class="SKUDeck___StyledDiv-sc-1e5d9gk-0 eA-dmzP"]') 
    for item in items:
        mouse_movement.human_click(page, item)

        #Name
        name_l = item.query_selector('//h3[@class="block m-0 line-clamp-2 font-regular text-base leading-sm text-darkOnyx-800 pt-0.5 h-full"]')
        name = name_l.inner_text().strip() if name_l else 'N/A'
        
        #Quantity
        quantity_l = item.query_selector('//span[@class="Label-sc-15v1nk5-0 PackChanger___StyledLabel-sc-newjpv-1 gJxZPQ cWbtUx"]')
        quantity = quantity_l.inner_text().strip() if quantity_l else 'N/A'

        #Discount
        discount_l = item.query_selector('//span[@class="font-semibold lg:text-xs xl:text-sm leading-xxl xl:leading-md"]')
        discount = discount_l.inner_text().strip() if discount_l else 'N/A'

        #Price
        price_l = item.query_selector('//span[@class="Label-sc-15v1nk5-0 Pricing___StyledLabel-sc-pldi2d-1 gJxZPQ AypOi"]')
        price = price_l.inner_text().strip() if price_l else 'N/A'

        #URL
        url_l = item.query_selector('//a[@href]')
        url = url_l.get_attribute('href') if url_l else "N/A"
        link = f"bigbasket.com{url}" if url else 'N/A'

        products.append({
            "Name": name,
            "Quantity": quantity,
            "Discount": discount,
            "Price": price,
            "Link": link
        })

        time.sleep(0.5)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1280, "height":800})
    page = context.new_page()
    stealth_sync(page)
    logging.info("Script started")

    page.set_extra_http_headers({
        "Accept-language": "en=US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    })

    page.goto("https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb", timeout=60000)
    page.wait_for_selector('//div[@class="grid grid-flow-col gap-x-6 relative mt-5 pb-5 border-t border-dashed border-silverSurfer-400"]', timeout=10000)

    for i in range(1, 5):
        get_data()
        url = f"https://www.bigbasket.com/cl/fruits-vegetables/?nc=nb&page={i+1}"
        page.goto(url, timeout=60000)
        page.wait_for_selector('//div[@class="grid grid-flow-col gap-x-6 relative mt-5 pb-5 border-t border-dashed border-silverSurfer-400"]', timeout=10000)

    context.close()
    browser.close()

filename = f"products{today}.csv"
df = pd.DataFrame(products)
df.to_csv(filename, index=False)

logging.info(f"CSV saved successfully: {filename}")
logging.info("Script execution completed")