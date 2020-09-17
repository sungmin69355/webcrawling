import requests
from bs4 import BeautifulSoup
#커밋 수 체크
url = 'https://github.com/sungmin69355'
req = requests.get(url)
 
html = req.text
soup = BeautifulSoup(html, 'html.parser')
#for tag in soup.select('h2[class="f4 text-normal mb-2"]'):
    #print(tag.text)


commit = 0
countArray =''

for i in range(1,10):
    countArray = 'rect[class="day"][data-count=\"'+ str(i)+'\"]'
    for tag in soup.select(countArray):
        commit+=1
        #print(tag.text)

print("1일 1커밋한 날은 총 "+str(commit)+"일입니다.")
