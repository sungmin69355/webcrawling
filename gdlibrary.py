import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def findpeople():
    driver = webdriver.Chrome('/Users/sungmin/chromedriver')
    driver.get('http://www.gdlibrary.or.kr/gilib/1000658/100049/bbsList.do')

    url = 'http://www.gdlibrary.or.kr/gilib/1000658/100049/bbsList.do'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    nowday = "2020-08-29"
    rank= 0
    ##첫페이지
    for tag in soup.select('td'):
        if tag.text == nowday:
            rank=rank+1

     ##두번쨰페이지
    driver.find_element_by_xpath("""//*[@id="listForm"]/div[2]/p/span[2]/a""").click()
    for tag in soup.select('td'):
        if tag.text == nowday:
            rank=rank+1
            
    ##세번째페이지
    driver.find_element_by_xpath("""//*[@id="listForm"]/div[2]/p/span[6]/a""").click()
    for tag in soup.select('td'):
        if tag.text == nowday:
            rank=rank+1

    print("오늘의 안심도서대출은 "+str(rank-1) +"명 입니다.")


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

