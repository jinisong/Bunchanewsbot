import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost',27017)
db = client.dbsparta

data = requests.get('https://e27.co/search/?s=vietnam')
soup = BeautifulSoup(data.text, 'html.parser')

url = soup.find('a',{'class':{'dark-anchor'}}).get('href')
print(url)
db.article.insert_one({'url': url})

#vnexpress에서 startup으로 검색한 가장 최근 기사의 url를 가져오는 코드_
data = requests.get('https://e.vnexpress.net/search?q=startup&media_type=all&cate_code=&search_f=title,lead&date_format=all&latest=on')         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'html.parser')

url1=soup.find('h4').a.get('href')
print(url1)

#Deal st.asia 검색어 vietnam 크롤링
data = requests.get('https://www.dealstreetasia.com/?s=vietnam')         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'html.parser')

article=soup.find('div',{'class':"col main-list-text-col"})
link = article.find_all('a')
url2=link[2].get('href')
print(url2)

#Deal st.asia 검색어 vietnam korea 크롤링
data = requests.get('https://www.dealstreetasia.com/?s=vietnam+korea')         # get 요청으로 html을 가져와라
soup = BeautifulSoup(data.text, 'html.parser')


article=soup.find('div',{'class':"col main-list-text-col"})
link = article.find_all('a')
url3=link[2].get('href')
print(url3)

