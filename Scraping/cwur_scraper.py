# Modules
from bs4 import BeautifulSoup
import requests

import csv

# Connect websites
def connect(URL):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", 
    }

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    rows = []
    ind = 0
    for el in soup.find_all("tr"):
        pos = 0
        for sub_el in el:
            text = sub_el.get_text()
            if pos == 0:
                rows.append([text])
            else:
                if pos == 1:
                    items = text.split('\n')
                    text = items[0]
                rows[ind].append(text)
            pos += 1
            if pos == 3:
                ind += 1
                break

    # Write to CSV
    header = ['University', 'Country', 'Rank']
    with open('cwur_ranking_19-20.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    URL = "https://cwur.org/2019-20.php"
    connect(URL)