# 🕵️ Email Scraper Dashboard

This project is a web-based tool for **automatically extracting email addresses** from public websites. It combines **Python web scraping**, a **Django web dashboard**, and **PostgreSQL** storage. It's great for practicing full-stack development, backend skills, and real-world automation.

---

## 🔍 Features

- ✅ Scrapes emails from both raw text and `mailto:` links  
- ✅ Saves results to PostgreSQL with timestamp and source URL  
- ✅ Displays results in a clean Django dashboard with pagination  
- ✅ Exports results to `scraped_emails.csv`  
- ✅ Configurable input list via `urls.txt`  
- ✅ Docker-ready for reproducible deployment  

---

## ⚙️ Tech Stack

- **Language**: Python 3.9  
- **Framework**: Django  
- **Database**: PostgreSQL  
- **Libraries**: `requests`, `BeautifulSoup`, `re`, `csv`  
- **Web UI**: HTML (Django Template), Pagination  
- **DevOps**: Docker (with `Dockerfile`)

---

## 🗂️ File Overview
Webscraper/
├── scraper.py # Main scraping logic
├── utils.py # Email extraction (regex)
├── urls.txt # List of target URLs
├── scraped_emails.csv # Output CSV file
├── Dockerfile # Docker config
├── requirements.txt # Dependencies
├── .env # Database credentials
├── manage.py # Django entry point
├── emailsite/ # Django project config
└── webapp/ # Django app: models, views, templates
