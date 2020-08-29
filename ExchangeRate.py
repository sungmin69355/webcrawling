import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for sel in soup.select('tr[class="dw"]'):
    print(sel.text)
