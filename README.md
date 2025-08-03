# 📬 Automated Email Scraper and CSV Export Tool

This project is a simple Python tool that scrapes public email addresses from a list of websites and saves the results to a CSV file. It helps automate the tedious task of gathering contact info for business outreach or research.

---

## ✅ Features

- Extracts email addresses from websites in `urls.txt`
- Automatically saves results to `scraped_emails.csv`
- Includes timestamp and source URL for each email
- Handles errors and skips inaccessible pages
- Optional integration with [Hunter.io](https://hunter.io) API (via `hunter.py`)

---

## 🧪 How to Use

### 1. Install dependencies

```bash
python3 -m pip install -r requirements.txt
