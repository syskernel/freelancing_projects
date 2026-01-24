# PROJECT 3 :🚗 boodmo car parts scraper

### 📁 Project Overview
The Boodmo Car Parts Scraper is a browser-automation-based data extraction tool designed to scrape detailed automobile spare parts information from Boodmo, one of India’s largest online car parts marketplaces.

Boodmo is a highly dynamic, JavaScript-driven platform with complex DOM structures and aggressive anti-bot mechanisms, making traditional scraping techniques unreliable. This project focuses on mastering advanced browser automation, DOM handling, and structured data extraction from real-world, production-grade e-commerce websites.

---

### 🎯 Objective
To build a Python automation script that:
* Searches car parts based on brand, model, and part category.
* Scrapes structured product details including:
    * Part name
    * Brand
    * Price
    * MRP
    * Discount
    * Availability
* Handles dynamic content loading, pagination, and infinite scroll.
* Stores clean and structured data in Excel / CSV format.
* Logs every execution step with timestamps for monitoring, debugging, and auditing.
* Scales to scrape 1000+ product records reliably.

---

### 🧩 Tech Stack
* Python (3.10+)
* NoDriver (Stealth Browser Automation)
* Chromium Browser Engine
* Python Libraries: asyncio, time, pandas, logging, openpyxl

---

### 🧾 Summary
This project is a high-complexity browser automation scraper built to extract structured automobile spare parts data from Boodmo.

Due to Boodmo’s dynamic rendering, shadow DOM usage, and continuous content updates, traditional request-based scraping and API sniffing approaches fail frequently. To overcome this, the scraper uses real browser simulation with NoDriver, enabling precise DOM interactions, JavaScript-rendered content access, and human-like browsing behavior.

The scraper intelligently waits for dynamic elements, extracts deeply nested product cards, handles pagination seamlessly, and ensures clean data formatting before exporting to Excel. Logging mechanisms are integrated to track execution flow, making debugging efficient and production-ready.

This project demonstrates advanced scraping engineering, real-world problem solving, and professional automation workflow design.

--- 

### 🚀 Future Enhancements
* Proxy Rotation & IP Pool Management
* Advanced Fingerprint Masking
* Parallel Scraping for Faster Throughput
* Analytics Dashboard for Market Insights
* Smart Retry & Failure Recovery System
* Cloud Deployment & Scheduled Automation

---