import asyncio
from playwright.async_api import async_playwright
import pandas as pd

all_properties = []

async def get_data(page, listing_number):
    print(f"Fetching data for listing {listing_number}")
    await page.wait_for_timeout(2000)
    property_data = {}

    for i in range(14):
        heading = page.locator('//td[@class="DataletSideHeading"]')
        data1 = (await heading.nth(i).inner_text()).strip()
        content = page.locator('//td[@class="DataletData"]')
        data2 = (await content.nth(i).inner_text()).strip()
        property_data[data1] = data2
    
    return property_data

async def save_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width":1280, "height":800})
        page = await context.new_page()  
        print("Script started")  

        await page.set_extra_http_headers({
            "Accept-language": "en=US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        })    

        print("Going to the site")
        await page.goto("http://delcorealestate.co.delaware.pa.us/PT/search/advancedsearch.aspx?mode=advanced", timeout=60000)
        await page.wait_for_load_state("networkidle")

        await page.click('//button[@id="btAgree"]')
        await page.wait_for_timeout(2000)

        await page.select_option("#sCriteria", label="School District")
        await page.select_option("#sPickList", label="S01 - Chester-Upland School District")
        await page.click('//button[@id="btAdd"]')
        await page.wait_for_timeout(1000)
        await page.select_option("#sCriteria", label="Square Feet")
        await page.type("#txtCrit", "0", delay=100)
        await page.type("#txtCrit2", "1000", delay=100)
        await page.click('//button[@id="btAdd"]')
        await page.wait_for_timeout(1000)
        await page.click('//button[@id="btSearch"]')
        await page.wait_for_timeout(2000)

        first = page.locator('//tr[@class="SearchResults"]').nth(0)
        await first.click()
        await page.wait_for_timeout(10000)

        for listing_number in range(100):
            data = await get_data(page, listing_number)
            all_properties.append(data)
            await page.click('//input[@id="DTLNavigator_imageNext"]')

        await context.storage_state(path="C:/browser_profiles/delaware.json")

        await context.close()
        await browser.close()

asyncio.run(save_session())

df = pd.DataFrame(all_properties)
df.to_csv("property_data.csv", index=False)
print("CSV saved successfully")