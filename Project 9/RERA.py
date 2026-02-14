import asyncio
from playwright.async_api import async_playwright

async def fetch_page(active_page):
    registr = await active_page.locator("//label[text()='Registration Number']/following-sibling::label").inner_text()
    print(registr)

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

        await page.goto("https://maharera.maharashtra.gov.in/projects-search-result", timeout=60000)
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
                print(active_page.url)
                print("You can Fetch data now")
            elif command == "fetch":
                await fetch_page(active_page)
            else:
                break

        await context.close()
        await browser.close()

asyncio.run(save_session())