import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import os

tender = []

async def aoc_page(active_page):
    #locator = active_page.locator("td.page_title", has_text="AOC Summary")
    locator = active_page.locator('tr:has(td:text("AOC Summary"))')
    count = await locator.count()
    if count > 0:
        print("Confirmed: AOC page")
        return True
    else:
        print("Not on AOC page")

async def fetch_page(active_page):
    organisation = (await active_page.locator("//td[text()='Organisation Chain']/following-sibling::td").inner_text()).strip()
    tender_id = (await active_page.locator("//td[text()='Tender ID : ']/following-sibling::td").inner_text()).strip() 
    title = (await active_page.locator("//td[text()='Tender Title : ']/following-sibling::td").inner_text()).strip() 
    date = (await active_page.locator("//td[text()='Contract Date : ']/following-sibling::td/b").inner_text()).strip() 
    period = (await active_page.locator("//td[text()='Work Completion Period (in days) : ']/following-sibling::td/b").inner_text()).strip()
    name = (await active_page.locator("//tr[@id='informal']/td[3]").inner_text()).strip()
    value = (await active_page.locator("//tr[@id='informal']/td[5]").inner_text()).strip()
    tender.append({
        "TENDER ID": tender_id,
        "NAME OF TENDER": title,
        "CONTRACT DATE": date,
        "CONTRACT VALUE": value,
        "WORK PERIOD(in days)": period,
        "ORGANISATION": organisation,
        "BIDDER NAME": name
    })
    print("successfully added details to file")

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

        #await page.goto("https://eprocure.gov.in/eprocure/app", timeout=60000)
        await page.goto("https://mahatenders.gov.in/nicgep/app", timeout=60000)
        await page.wait_for_load_state("networkidle")

        async def handle_new_page(new_page):
            nonlocal active_page
            await new_page.wait_for_load_state("domcontentloaded")
            active_page = new_page

        context.on(
            "page",
            lambda new_page: asyncio.create_task(handle_new_page(new_page))
        )

        n = 0
        while True:
            n += 1
            print(n)
            command = await asyncio.to_thread(input, "Enter command: ")
            if command == "fetch":
                if await aoc_page(active_page) == True:
                    print(active_page.url)
                    await fetch_page(active_page)
            else:
                break
        
        await context.close()
        await browser.close()

asyncio.run(save_session())

new_df = pd.DataFrame(tender)
filename = "tenders_master01.xlsx"
if os.path.exists(filename):
    old_df = pd.read_excel(filename)
    combined_df = pd.concat([old_df, new_df]).drop_duplicates()
    combined_df.to_excel(filename, index=False)
else:
    new_df.to_excel(filename, index=False)

print("CSV saved Successfully!")