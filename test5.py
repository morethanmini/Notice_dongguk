import requests
from bs4 import BeautifulSoup #BeautifulSoup는 HTML 페이지의 웹소스를 쉽게 파싱 할 수 있도록 도와주는 라이브러리입니다.
import telegram

bot = telegram.Bot(token='bot token')

req = requests.get('https://web.dongguk.ac.kr/mbs/kr/jsp/board/list_all.jsp?boardId=0&id=kr_070101000000')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.find("table", {"class": "list"})
"""
find_all로 찾게 되면 배열로 결과가 리턴됩니다. 그래서 이렇게 하나의 요소만 있을 때는 find로 하여 바로 object를 받을 수 있게 하면 좋습니다.
find_all() 함수에서 class_ 옵션을 사용하면 위의 코드처럼 특정 클래스가 포함된 문자열이 포함되어 검색되기 때문에 검색의 범위를 좁힐 수 있다.

select 해당 내용이 리스트로 묶여 나오고, select_one은 리스트안의 값을 추출 할 수 있다.
select_one은 그리고 문서의 처음부터 시작하여 조건에 맞는 하나를 찾게 된다. 
반면 select는 모든 a태그를 찾아 리스트에 담게 된다.
따라서 select_one은 바로 .text ["href"] 등을 적용하는 것이 가능하다.
하지만 select의 경우에는 for 문을 통해 다시 개별요소에 접근을 해야한다.

title = posts.select_one('td[class$="subject"]').text / $를 쓰면 ""로 끝나는 값을 찾을 수 있다.
css seletor에서 :not()을 사용
"""

title = posts.select_one('td.subject:not(.subject.new)').text
link = 'https://web.dongguk.ac.kr/mbs/kr/jsp/board/' + posts.select_one('td.subject:not(.subject.new) > a')['href']

text = "<글 업데이트>" + "\n" + title + link
bot.sendMessage(-1001250905630, text)

print(text)