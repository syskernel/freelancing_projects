# PROJECT 7 : 🏢 Datacentre Location Scraper

### 📁 Project Overview
This project is a browser-automation-based web scraping system built using Playwright (Python) to extract structured information about data center facilities from a JavaScript-heavy website.

Modern listing websites rely on client-side rendering, dynamic pagination, delayed DOM hydration, and interactive UI components, making traditional request-based scraping unreliable. This project uses real browser automation to reliably navigate paginated listings, detect pagination state, and extract data in a controlled, production-ready manner.

The scraper is designed with clear control flow, async-safe pagination, and logging support, making it suitable for long-running scraping tasks and future scalability

---

### 🎯 Objective
To build a robust Python automation system that:
1.Navigates through all paginated listing pages using Playwright.
2.Detects the last page accurately by inspecting button state (disabled pagination).
3.Extracts structured data such as:
  * Data center name
  * Provider
  * Address / location details
4.Logs scraping progress, pagination steps, and execution flow for debugging and traceability.
5.Multiple locations can easily be searched by just adding new keywords.
6.Avoids infinite loops and duplicate scraping through deterministic pagination logic.

---

### 🧩 Tech Stack
* Python (3.10+)
* Playwright (Async Browser Automation)
* Chromium Browser Engine
* AsyncIO (Event loop management)
* Logging (Script execution & pagination tracking)
* Standard Libraries: time, pandas, logging

---

### 🧾 Summary
This project demonstrates a real-world pagination-aware scraping workflow using Playwright’s async API. Instead of relying on DOM presence alone, the scraper determines pagination termination by inspecting the disabled state of the “Next” button, ensuring accurate stopping conditions.
The scraper follows a clean separation of concerns:
  * Navigation and pagination logic is isolated into reusable async functions.
  * Data extraction is scoped to individual listing cards using relative selectors.
  * Logging provides visibility into page traversal, scraping progress, and exit  conditions.
By using a single browser context and controlled navigation, the script mimics realistic user behavior while maintaining efficiency and stability. This structure closely resembles production scraping pipelines used in freelancing, internal tooling, and automation systems.

---

### 🚀 Future Enhancements
* Google Sheets / Excel Integration for structured data storage
* Proxy Rotation & IP Management
* Enhanced Logging (success/failure per page or item)
* Screenshot & HTML Snapshot Capture for Debugging
* Advanced Browser Stealth & Fingerprint Control
* Retry Logic for Failed Pages
* Pagination Metrics (page count, item count validation)
* Database Integration (SQLite / PostgreSQL)
* Scheduled Runs via Cron / Task Scheduler
* Automated Data Cleaning & Validation

---