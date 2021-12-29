import telegram

"""
token = '1787374542:AAHTkUuO3qKc5HlczhsNwRkhYf1pycuncIY'
bot = telegram.Bot(token=token)

#생성한 텔레그램 봇 정보
me = bot.getMe()
print(me)

#생성한 텔레그램 봇 /start 시작 후 사용자 id 받아 오기
chat_id = bot.getUpdates()[-1].message.chat.id
print('user id :', chat_id)

#bot.sendMessage(chat_id='1710902272', text='안녕!!')

# 오류가 나면 챗봇에 /start 실행
"""

token = "1787374542:AAHTkUuO3qKc5HlczhsNwRkhYf1pycuncIY"
bot = telegram.Bot(token = token)
updates = bot.get_updates()
for u in updates:
    print(u.message['chat']['id'])