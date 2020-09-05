import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for sel in soup.select('tr[class ="dw"]'):
    print(sel.text)
for sel in soup.select('tr[class ="up"]'):
    print(sel.text)

#미국
for sel in soup.select('#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr.dw > td:nth-child(2) > span'):
    print(sel.text)

#일본
for sel in soup.select('#_cs_foreigninfo > div > div.contents03_sub > div > div.c_rate > div.rate_table_bx._table > table > tbody > tr:nth-child(2) > td:nth-child(2) > span'):
    print(sel.text)
