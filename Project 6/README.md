# PROJECT 6 :🐶 Petsmart dog food scraper

### 📁 Project Overview
This project is a browser-automation-based scraping and data enrichment pipeline designed to process large batches of URLs stored in an Excel file and extract structured information from each website using Playwright.

Modern websites rely heavily on JavaScript rendering, dynamic DOM updates, delayed content loading, and bot-detection mechanisms, making request-based scraping unreliable. This project focuses on building a robust, resumable, and production-ready automation workflow that mimics real user behavior while reliably enriching an existing Excel dataset with newly fetched information.

---

### 🎯 Objective
To build a Python automation system that:
  1.Reads 800+ URLs from an existing Excel file.
  2.Visits each website using Playwright browser automation.
  3.Extracts required data (e.g. product name, prices, sizes, flavor, brand and ingredients/nutrients).
  4.Is scalable, maintainable, and suitable for long-running scraping jobs.

---

### 🧩 Tech Stack
* Python (3.10+)
* Playwright (Browser Automation)
* Chromium Browser Engine
* Pandas (Excel read/write & data handling)
* OpenPyXL (Excel engine)
* Standard Libraries: pathlib, time, logging

---

### 🧾 Summary
This project demonstrates a real-world scraping and automation workflow where Excel acts as a lightweight database and Playwright functions as a reliable data fetcher for JavaScript-heavy websites.

Instead of creating new output files for every run, the system enriches an existing Excel file, ensuring continuity, resumability, and transparency. Each URL is processed sequentially using a single browser context for efficiency and lower detection risk.

Key features include intelligent wait strategies, DOM-aware automation, structured dataframe updates, failure handling, and checkpoint-based progress saving. This approach closely mirrors how professional scraping pipelines are built for freelancing, data operations, and long-term automation projects.

---

### 🚀 Future Enhancements
* Proxy Rotation & IP Management
* Logs success and failure states for each URL
* Advanced Browser Stealth & Fingerprint Control 
* Updating the same Excel file by appending new columns while preserving old data
* Asynchronous / Parallel URL Processing
* HTML Snapshot Storage for Debugging 
* SQLite / Database Integration
* Cloud Scheduling & Cron Automation
* Automated Data Validation & Cleaning

---