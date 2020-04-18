""" 
BeautifulSoupでWEBスクレイピング
WEBスクレイピングで有名なライブラリ
Webページのタグを見て、どのようなものがあるのかを解析する
"""

from bs4 import BeautifulSoup
import requests

html = requests.get('https://pigblog.org/')
# print(html.text)

soup = BeautifulSoup(html.text, 'lxml')
titles = soup.find_all('title')
print(titles[0].text)

contetns = soup.find_all('h2', {'class': 'e-card-title'})

for content in contetns:
    print(content.text)
