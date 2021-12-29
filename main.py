#동국 공지사항 알리미
import requests
from bs4 import BeautifulSoup
import time
import telegram
import datetime

bot = telegram.Bot(token='bot token')

if __name__ == '__main__':
    latest_title = 0
    while True:
        req = requests.get('https://web.dongguk.ac.kr/mbs/kr/jsp/board/list_all.jsp?boardId=0&id=kr_070101000000')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("table", {"class": "list"})
        post_title = posts.select_one('td.subject:not(.subject.new)').text

        link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.select_one('td.subject:not(.subject.new) > a').attrs['href']

        if latest_title != post_title:
            latest_title = post_title

            title = posts.select_one('td.subject:not(.subject.new)').text
            link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.select_one('td.subject:not(.subject.new) > a').attrs['href']

            text = "<글 업데이트>" + "\n" + title + link

            bot.sendMessage(-1001250905630, text)

            print(title)
            print(link)

        time.sleep(600)

        now = datetime.datetime.now()
        nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
        print("\n마지막 글" + latest_title + "update : " + nowDateTime)