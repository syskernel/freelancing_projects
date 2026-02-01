import asyncio
from playwright.async_api import async_playwright
import pandas as pd

datacentre = []

async def next_button(page):
    nxt_btn = await page.query_selector('//button[@data-testid="next-page-button"]')
    if not nxt_btn:
        return False

    is_disabled = await nxt_btn.is_disabled()
    if is_disabled:
        return False

    await nxt_btn.click()
    await page.wait_for_load_state("networkidle")
    return True

async def get_data(page):
    items = await page.query_selector_all('//a[@class="flex flex-col gap-2 rounded border border-gray-100 p-2 hover:border-teal-300 hover:shadow-lg hover:shadow-teal-600/40"]')
    for item in items:
        box = await item.query_selector('//div[@class="flex flex-col gap-2"]')
        name_l = await box.query_selector('//div[@class="text font-medium hover:text-purple"]')
        name = (await name_l.inner_text()).strip() if name_l else 'N/A'

        meta = await box.query_selector_all('//div[@class="text-xs text-gray-500"]')

        provider = (await meta[0].inner_text()).strip() if len(meta) > 0 else 'N/A'
        adress = (await meta[1].inner_text()).strip() if len(meta) > 1 else 'N/A'

        datacentre.append({
            "NAME": name,
            "PROVIDER": provider,
            "ADDRESSS": adress
        })

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
        while True:
            await page.wait_for_selector('//div[@data-testid="container"]', timeout=10000)
            await get_data(page)
            has_next = await next_button(page)
            if not has_next:
                break

        await context.storage_state(path="C:/browser_profiles/session.json")

        await context.close()
        await browser.close()

asyncio.run(save_session())

df = pd.DataFrame(datacentre)
df.to_csv("datacentre.csv", index=False)
print("All details successfully saved to datacentre.csv")