import requests
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%96%A5%EC%88%98%EC%B6%94%EC%B2%9C&oquery=%ED%96%A5%EC%88%98&tqi=U0U83wp0J14ssQHBwadssssssPC-492634'
req = requests.get(url)
 
html = req.text
soup = BeautifulSoup(html, 'html.parser')

rank= 1
for tag in soup.select('span[class="tit"]'):
    print(str(rank)+"등 " + tag.text)
    rank+=1
    if rank == 11:
        break