import re

# 用正则表达式从普通文本中找出所有形如 xxx@xxx.com 的邮箱，供 scraper.py 调用
def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)
