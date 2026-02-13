import asyncio
from playwright.async_api import async_playwright

async def save_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width":1280, "height":800})
        page = await context.new_page()

        await page.set_extra_http_headers({
            "Accept-language": "en=US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        })    

        await page.goto("https://eprocure.gov.in/eprocure/app", timeout=60000)
        await page.wait_for_load_state("networkidle")
        #await page.wait_for_selector("#tender-details")
        await asyncio.sleep(100000)

asyncio.run(save_session())