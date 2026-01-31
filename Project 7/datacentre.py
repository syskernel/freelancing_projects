import asyncio
from playwright.async_api import async_playwright
import time

async def save_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width":1280, "height":800})
        page = await context.new_page()    

        await page.set_extra_http_headers({
            "Accept-language": "en=US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        })    

        await page.goto("https://www.datacenters.com/locations/australia", timeout=60000)
        await page.wait_for_load_state("networkidle")
        #await page.wait_for_selector('//div[@data-testid="container"]', timeout=10000)
        #items = await page.query_selector_all('//a[@class="flex flex-col gap-2 rounded border border-gray-100 p-2 hover:border-teal-300 hover:shadow-lg hover:shadow-teal-600/40"]')
        nxt_btn = await page.query_selector('//button[@data-testid="next-page-button"]')
        await nxt_btn.click()
        time.sleep(3)

        await context.storage_state(path="C:/browser_profiles/session.json")

        await context.close()
        await browser.close()

asyncio.run(save_session())