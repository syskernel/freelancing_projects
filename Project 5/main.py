from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import pandas as pd
import time
import mouse_movement

job_data = []
v = 0

def get_data():
    # Select all job listing containers
    job_cards = page.query_selector_all('//div[@data-testid="slider_item"]')
    print(f"Total jobs found: {len(job_cards)}")

    for job in job_cards:
        # Job Title
        title_el = job.query_selector('//h2[@class="jobTitle css-bl7gmb eu4oa1w0"]')
        title = title_el.inner_text().strip() if title_el else 'N/A'
 
        # Company Name
        company_el = job.query_selector('//span[@data-testid="company-name"]')
        company = company_el.inner_text().strip() if company_el else 'N/A'

        # Location
        location_el = job.query_selector('//div[@data-testid="text-location"]')
        location = location_el.inner_text().strip() if location_el else 'N/A'

        # Salary
        salary_el = job.query_selector('//div[@data-testid="attribute_snippet_testid"]')
        salary = salary_el.inner_text().strip() if salary_el else 'N/A'

        # URL
        inner_tag = job.query_selector('a[data-jk]')
        job_key = inner_tag.get_attribute('data-jk') if inner_tag else None
        job_url = f"https://in.indeed.com/viewjob?jk={job_key}&from=shareddesktop_copy" if job_key else 'N/A'

        mouse_movement.human_click(page, job)
        time.sleep(2)

        job_data.append({"Title": title,
                         "Company": company,
                         "Location": location,
                         "Salary": salary,
                         "URL": job_url
                         })

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    stealth_sync(page)

    # Set headers to appear as a real browser
    page.set_extra_http_headers({
        "Accept-Language": "en-US,en;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })

    # Load Indeed jobs page
    page.goto("https://in.indeed.com/jobs?q=python+developer&l=Banglore%2C+Karnataka&radius=25", timeout=60000)
    #page.wait_for_selector('//div[@id="mosaic-jobResults"]', timeout=10000)
    page.wait_for_selector('//div[@class="jobsearch-LeftPane css-1m1zdkx eu4oa1w0"]', timeout=10000)
    mouse_movement.human_scroll(page, amount=800)

    for i in range(1, 10):
        v += 10
        print(f"Getting data from page {i}")
        page.mouse.wheel(0, 1000)
        time.sleep(2)

        get_data()

        new_url = f"https://in.indeed.com/jobs?q=python+developer&l=Banglore%2C+Karnataka&radius=25&start={v}"
        page.goto(new_url, timeout=60000)
        stealth_sync(page)
        mouse_movement.human_scroll(page, amount=800)
        time.sleep(2)

        page.wait_for_selector('//div[@class="jobsearch-LeftPane css-1m1zdkx eu4oa1w0"]', timeout=10000)
        
    context.close()
    browser.close()

df = pd.DataFrame(job_data).drop_duplicates()
df.to_csv("job_data2.csv", index=False)

print(f"CSV saved successfully")