from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import pandas as pd

datacentres = []
location = ("australia", "new-zealand")

def get_data():
    cards = page.query_selector_all('//a[@class="flex flex-col gap-2 rounded border border-gray-100 p-2 hover:border-teal-300 hover:shadow-lg hover:shadow-teal-600/40"]')

    for card in cards:
        #name
        name_el = card.query_selector('//div[@class="text font-medium hover:text-purple"]')
        name = name_el.text_content().strip() if name_el else "N/A"

        #address
        address_el = card.query_selector_all('//div[@class="text-xs text-gray-500"]')
        address = address_el[1].text_content().strip()

        #image
        image_el = card.query_selector('//img[@src]')
        image = image_el.get_attribute('src') if image_el else "N/A"

        datacentres.append({
            "NAME": name,
            "ADDRESS": address,
            "IMAGE": image,
            "POWER OUTPUT": "N/A"
        })
        
# Launching Browser
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport=
                                  {"width":1280, "height":800})
    page = context.new_page()
    stealth_sync(page)

    page.set_extra_http_headers({
        "Accept-Language": "en=US,en:q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
    })

    for country in location:
        n = 1
        url = f"https://www.datacenters.com/locations/{country}"
        page.goto(url, timeout=60000)

        while True:
            print(f"Getting data of page {n} from {country}")
            n += 1
            get_data()
            next_button = page.query_selector('//button[@class="Control__control__ijHLR Pagination__pageItem__NsQSw Pagination__symbol__KHv6r"]')
            # Ask user what to do next
            user_input = input("➡️  Click 'Next' in the browser manually, then press Enter to continue (or type 'stop' to end): ")

            if user_input.strip().lower() == "stop":
                print(f"Stopping scrape for {country}.")
                break

            # Wait for the new page data to load after your manual click
            try:
                page.wait_for_selector('//a[@class="flex flex-col gap-2 rounded border border-gray-100 p-2 hover:border-teal-300 hover:shadow-lg hover:shadow-teal-600/40"]', timeout=10000)
            except:
                print("⚠️  Timed out waiting for new page, assuming no more pages.")
                break

    context.close()
    browser.close()

df = pd.DataFrame(datacentres).drop_duplicates()
df.to_csv("datacentres.csv", index=False)
print(f"All data saved to datacentres.csv")

import requests
import json

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Cache-Control": "no-cache",
        "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}

url = "https://www.datacenters.com/api/v1/locations/countries/12?query=&page=2&sort_by=preloaded_search_locations.recent_visits_count&sort_direction=desc&radius=100"
resp = requests.get(url, headers=headers)

data = resp.json()

with open("datacentre.json", "w") as f:
    json.dump(data, f, indent=4)
    
print("SAVED JSON Data in datacentre.json")