import requests
from bs4 import BeautifulSoup
import time

class title_links:
    def get_title(self):
        url = f'https://web.dongguk.ac.kr/mbs/kr/jsp/board/list_all.jsp?boardId=0&id=kr_070101000000'
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        #title = soup.find("tbody").find_all(class_='subject')
        title = soup.find("tbody").find_all('tr')
        #itle = soup.select("tbody")

        for i in title:
            text = i.select("td.subject")[0].text
            href = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + i.select("a")[0].attrs['href']

            hyper = text + href
            print(hyper)

a = title_links()
a.get_title()