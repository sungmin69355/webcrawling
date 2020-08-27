import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime

#driver = webdriver.Chrome(executable_path='c:/Users/sungmin/chromedriver')
#driver.get('https://www.naver.com (https://www.naver.com/)')

url = 'http://www.gdlibrary.or.kr/gilib/1000658/100049/bbsList.do'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')



rank= 1
now = datetime.datetime.now()
nowday1 = (str(now.year)+"-"+str(now.month)+"-"+str(now.day))
nowday = "2020-08-27"

for tag in soup.select('td'):
    if nowday == tag.text:
        rank=rank+1
    
for page in soup.select('a'):
    print(page.text)

#<a href="#" onclick="goPage(2); return false;">2</a>
print("오늘의 안심도서대출은 "+str(rank) +"명 입니다.")
