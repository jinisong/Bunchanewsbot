import requests
from bs4 import BeautifulSoup
import telegram
from telegram.ext import Updater, MessageHandler, Filters




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



my_token = '729010308:AAGj0mPUkmRaf19gr3LLP9Wj8tYGbn69_w0'
newsbot = telegram.Bot(token = my_token)

def get_message(bot, update) :
    update.message.reply_text("뉴스를 보냅니다.")
    update.message.reply_text(url1)
    update.message.reply_text(url2)
    update.message.reply_text(url3)

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()
