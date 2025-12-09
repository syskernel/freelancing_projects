# PROJECT 2 :🧺 Big Basket product scraper

### 📁 Project Overview
The BigBasket Product Scraper is a Playwright-based automation tool designed to extract product information—such as product name and price—from BigBasket’s category pages.

BigBasket is known for having strict bot-detection systems, which makes scraping challenging for beginners.
This project focuses on understanding and implementing realistic browser behavior to reduce detection, while learning how to extract structured data from a modern, JavaScript-heavy website.

---

### 🎯 Objective
To build a Python script that automatically:
1. Get results for specific category **Fruits and Vegetables**.
2. Scrapes details such as name, quantity, price, discount and url.
3. Script can be modified for getting 1000+ results.
4. Saves the data in a structured CSV format for further analysis or marketing research.
5. Everytime the script runs it logs extraction steps and saves it as the present date.

---

### 🧩 Tech Stack
1. Python (3.10+)
2. Playwright (Python)
3. Playwright Stealth
4. Browser Engine: Chromium
5. Python Libraries: time, logging, pandas

---

### 🧾 Summary
This project is a Playwright-based web scraper designed to extract product data from BigBasket’s Fruits & Vegetables category. The scraper uses stealth techniques, custom headers, and non-headless browsing to reduce detection and avoid 403 / access-denied errors.

It supports pagination, allowing the script to navigate through multiple pages automatically and extract product details such as name, price, and SKU card info.

The scraper includes a simple logging system to track each step—page visits, successful scrapes, and errors—to make debugging easier and progress transparent.

This project demonstrates how to scrape modern, JavaScript-heavy e-commerce websites reliably using Playwright, while handling basic anti-bot defenses and maintaining clarity through structured logs.

---

### 🚀 Future Enhancements
* 🔄 Auto-Rotation of Proxies
* 🧠 Smarter Anti-Bot Evasion
* 📊 Dashboard for Monitoring
* ⚙️ Error Recovery & Retry Logic
* 🚨 Alerting System

---