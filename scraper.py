import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emailsite.settings")
django.setup()

import requests
from bs4 import BeautifulSoup
from utils import extract_emails
from datetime import datetime
import csv

def scrape_emails_from_url(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 1. 从纯文本中提取邮箱
        emails_text = extract_emails(soup.get_text())

        # 2. 从 mailto 链接中提取邮箱
        emails_links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('mailto:'):
                email = href.replace('mailto:', '').split('?')[0]
                emails_links.append(email)

        # 3. 合并并去重
        emails = list(set(emails_text + emails_links))
        timestamp = datetime.utcnow().isoformat()

        # 4. 构造结果
        results = []
        for email in emails:
            results.append({
                "email": email,
                "source_url": url,
                "timestamp": timestamp
            })
        return results

    except Exception as e:
        print(f"❌ Error scraping {url}: {e}")
        return []

def main():
    with open("urls.txt", "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    
    all_results = []
    for url in urls:
        results = scrape_emails_from_url(url)
        all_results.extend(results)

    # 写入 CSV 文件
    with open("scraped_emails.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["email", "source_url", "timestamp"])
        writer.writeheader()
        writer.writerows(all_results)

     # 保存到数据库
    from webapp.models import EmailEntry
    for entry in all_results:
        EmailEntry.objects.create(
            email=entry["email"],
            source_url=entry["source_url"],
            timestamp=entry["timestamp"]
        )    

    print(f"✅ Done. Extracted {len(all_results)} emails. Output saved to scraped_emails.csv")

if __name__ == "__main__":
    main()
