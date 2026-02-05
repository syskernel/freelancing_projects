import asyncio
from playwright.async_api import async_playwright
import logging
import time

async def save_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width":1280, "height":800})
        page = await context.new_page()  
        logging.info("Script started")  

        await page.set_extra_http_headers({
            "Accept-language": "en=US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        })    

        logging.info("Going to the site")
        await page.goto("http://delcorealestate.co.delaware.pa.us/PT/search/advancedsearch.aspx?mode=advanced", timeout=60000)
        await page.wait_for_load_state("networkidle")

        await page.click('//button[@id="btAgree"]')
        time.sleep(10)

        await page.select_option("#sCriteria", label="School District")
        await page.select_option("#sPickList", label="S01 - Chester-Upland School District")
        await page.click('//button[@id="btAdd"]')
        time.sleep(1)
        await page.select_option("#sCriteria", label="Square Feet")
        await page.type("#txtCrit", "0", delay=100)
        await page.type("#txtCrit2", "1000", delay=100)
        await page.click('//button[@id="btAdd"]')
        time.sleep(1)
        await page.click('//button[@id="btSearch"]')
        time.sleep(2)

        search_results = await page.query_selector_all('//tr[@class="SearchResults"]')
        for result,i in enumerate(search_results):
            await result[i].click()

        await context.storage_state(path="C:/browser_profiles/delaware.json")

        await context.close()
        await browser.close()

asyncio.run(save_session())