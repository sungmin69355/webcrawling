import requests
from bs4 import BeautifulSoup
#무신사 검색어 순위 검색
url = 'https://github.com/sungmin69355'
req = requests.get(url)
 
html = req.text
soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('h2[class="f4 text-normal mb-2"]'):
    print(tag.text)