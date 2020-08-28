import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime


def findpeople():
    
    driver = webdriver.Chrome('/Users/sungmin/chromedriver')
    driver.get('http://www.gdlibrary.or.kr/gilib/1000658/100049/bbsList.do')
    
    url = 'http://www.gdlibrary.or.kr/gilib/1000658/100049/bbsList.do'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    nowday = "2020-08-27"
    rank= 0
    for tag in soup.select('td'):
        if tag.text == nowday:
            rank=rank+1

    driver.find_element_by_xpath("""//*[@id="listForm"]/div[2]/p/span[2]/a""").click()
    for tag in soup.select('td'):
        if tag.text == nowday:
            rank=rank+1

    for page in range(4,14):
        driver.find_element_by_xpath("""//*[@id="listForm"]/div[2]/p/span[""" +str(page)+"""]/a""").click()
        for tag in soup.select('td'):
            if tag.text == nowday:
                rank=rank+1
    print("어제의 안심도서대출은 "+str(rank) +"명 입니다.")


findpeople()


""""
//*[@id="listForm"]/div[2]/p/span[4]/a
//*[@id="listForm"]/div[2]/p/span[5]/a
//*[@id="listForm"]/div[2]/p/span[6]/a
//*[@id="listForm"]/div[2]/p/span[7]/a
//*[@id="listForm"]/div[2]/p/span[8]/a
//*[@id="listForm"]/div[2]/p/span[12]/a
//*[@id="listForm"]/div[2]/p/span[4]/a
rank= 0
now = datetime.datetime.now()
nowday1 = (str(now.year)+"-"+str(now.month)+"-"+str(now.day))
nowday = "2020-08-28"
"""

