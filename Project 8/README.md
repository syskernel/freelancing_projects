# PROJECT 8 : 🏠 Delaware Property Scraper

### 📁 Project Overview
This project is a browser-automation-based property data extraction system built using Playwright (Python) to scrape structured real estate information from a government property records website.

Unlike static HTML pages, property record portals rely heavily on dynamic navigation, session-based page transitions, JavaScript-triggered content rendering, and internal navigation controls (e.g., “Next Record” buttons). Traditional request-based scraping methods fail to handle these interactive flows reliably.

This scraper uses real browser automation to navigate search results, open property detail pages, paginate through listings using in-page navigation controls, and extract structured property data in a stable and scalable manner.

The project is designed with clean async architecture, proper separation of pagination and extraction logic, and structured data handling compatible with Pandas and CSV export workflows.

---

### 🎯 Objective
To build a structured, pagination-aware property scraping system that:
1. Aggregates multiple listings into a scalable list-of-dictionaries structure.
2. Navigates property search results and opens individual listing detail pages.
3. Iterates through property records using controlled “Next” navigation.
4. Extracts structured property-level data.
5. Dynamically captures heading–value table data without hardcoding field names.
6. Prevents data overwriting by isolating per-property dictionaries.
7. Converts extracted data into a clean Pandas DataFrame for CSV export.
8. Maintains deterministic flow to avoid infinite loops or duplicate scraping.

---

### 🧩 Tech Stack
* Python (3.10+)
* Playwright (Async Browser Automation)
* Chromium Browser Engine
* AsyncIO (Event loop handling)
* Pandas (Data structuring & CSV export)
* Standard Libraries: time, logging

---

### 🧾 Summary
This project demonstrates a real-world property scraping architecture using Playwright’s async API. Instead of scraping static HTML responses, the system navigates through interactive property detail views and extracts structured tabular data directly from dynamically rendered pages.
By mimicking real user navigation within a single browser session, the scraper maintains stability while handling session-based content. This structure reflects real-world automation pipelines used in freelance scraping projects, internal property data tools, and scalable data collection systems.

---

### 🚀 Future Enhancements
* Automated Parcel Search by Multiple Criteria
* Headless + Headed Mode Switching via CLI Flags
* Intelligent Stop Condition (Detect Last Record Automatically)
* Duplicate Record Detection
* Structured Logging Per Property
* Retry & Failure Handling Logic
* Proxy & IP Rotation Support
* Database Storage (SQLite / PostgreSQL)
* Scheduled Execution via Cron / Task Scheduler
* Data Validation & Cleaning Pipeline
* API Layer to Serve Scraped Property Data

---