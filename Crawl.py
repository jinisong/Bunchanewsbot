import requests
from bs4 import BeautifulSoup

#vnexpress에서 startup으로 검색한 가장 최근 기사의 메타데이터를 가져오는 코드_
data = requests.get('https://e.vnexpress.net/search?q=startup&media_type=all&cate_code=&search_f=title,lead&date_format=all&latest=on')         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'html.parser')

url=soup.find('h4').a.get('href')

data = requests.get(url)         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'html.parser')    # 가져온 html을 BeautifulSoup 라이브러리로 예쁘게 만들자

title1 = soup.find("meta",  property="og:title")
desc1 = soup.find("meta",  property="og:description")
image1 = soup.find("meta",  property="og:image")

print(title1['content'])
print(desc1['content'])
print(image1['content'])