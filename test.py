import requests
from bs4 import BeautifulSoup
import time
import telegram

bot = telegram.Bot(token='1787374542:AAHTkUuO3qKc5HlczhsNwRkhYf1pycuncIY')

if __name__ == '__main__':
    latest_num = 0
    while True:
        req = requests.get('https://web.dongguk.ac.kr/mbs/kr/jsp/board/list.jsp?boardId=106&id=kr_070103000000')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        posts = soup.find("tbody").find_all('tr')

        for i in posts:
            text = i.select("td.subject")[0].text
            href = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + i.select("a")[0].attrs['href']

            hyper = text + href

            print(hyper)

            bot.sendMessage(-1001250905630, hyper)
            time.sleep(10)
