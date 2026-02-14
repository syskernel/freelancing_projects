import asyncio
from playwright.async_api import async_playwright

async def aoc_page(active_page):
    locator = active_page.locator("td.page_title", has_text="AOC Summary")
    count = await locator.count()
    if count > 0:
        print("Confirmed: AOC page")
        return True
    else:
        print("Not on AOC page")

async def fetch_page(active_page):
    pass

async def save_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(viewport={"width":1280, "height":800})
        page = await context.new_page()
        active_page = page

        await page.set_extra_http_headers({
            "Accept-language": "en=US,en;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
        })    

        await page.goto("https://eprocure.gov.in/eprocure/app", timeout=60000)
        await page.wait_for_load_state("networkidle")

        async def handle_new_page(new_page):
            nonlocal active_page
            await new_page.wait_for_load_state("domcontentloaded")
            active_page = new_page

        context.on(
            "page",
            lambda new_page: asyncio.create_task(handle_new_page(new_page))
        )

        while True:
            command = await asyncio.to_thread(input, "Enter command: ")
            if command == "page url":
                if await aoc_page(active_page) == True:
                    print(active_page.url)
                    print("You can Fetch data now")
            else:
                break
        
        await context.close()
        await browser.close()

asyncio.run(save_session())