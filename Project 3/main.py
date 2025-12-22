from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

with sync_playwright as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width":1280, "height":800})
    page = context.new_page()
    stealth_sync(page)

    page.set_extra_http_headers({
        "Accept-language": "en=US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
    })

    page.goto(,timeout=60000)
    page.wait_for_selector(,timeout=1000)

    glasses_card = page.query_selector_all()
    print(f"Total glasses found: {len(glasses_card)}")
     