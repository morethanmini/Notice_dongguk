import requests
from bs4 import BeautifulSoup
import time
import telegram
import datetime

bot = telegram.Bot(token='bot token')

if __name__ == '__main__':
    latest_num = 0
    while True:
        req = requests.get('https://web.dongguk.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=106&id=kr_070103000000')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("table", {"class": "list"})
        post_title = posts.find('td', class_='subject').get_text()

        if latest_num != post_title:
            latest_num = post_title

            title = posts.find('td', class_='subject').text
            link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.find("a").attrs['href']
            hyper = title + link

            text = "<글 업데이트>" + "\n" + title + "\n" + link

            bot.sendMessage(-1001250905630, text)

            print(hyper)

        time.sleep(5)

        now = datetime.datetime.now()
        nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("\n 마지막 글" + latest_num + "update : " + nowDateTime)