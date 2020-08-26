import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
#무신사 검색어 순위 검색
url = 'https://store.musinsa.com/app/usr/search_ranking'
req = requests.get(url)
 
html = req.text
soup = BeautifulSoup(html, 'html.parser')

rank= 1
for tag in soup.select('span[class="word"]'):
    print(str(rank)+"등 " + tag.text)
    rank+=1
