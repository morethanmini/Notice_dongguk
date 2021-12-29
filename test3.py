import requests
from bs4 import BeautifulSoup
import time
import telegram

bot = telegram.Bot(token='bot token')


req = requests.get('https://web.dongguk.ac.kr/mbs/kr/jsp/board/list_all.jsp?boardId=0&id=kr_070101000000')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.find("table", {"class": "list"})
#post_title = posts.find('td', class_='subject').get_text()
post_link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.find("a").attrs['href']
title = posts.select('td[class="subject"]')

for i in title:
    post_title = i.text
    #post_link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.find("a").attrs['href']
    href = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + i.select("a")[0].attrs['href']

    text = "<게시글 업데이트>" + post_title + "\n" + href
    bot.sendMessage(-1001250905630, text)

    print(text)
