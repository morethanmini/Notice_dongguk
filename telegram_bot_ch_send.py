import telegram

token = '1787374542:AAHTkUuO3qKc5HlczhsNwRkhYf1pycuncIY'
bot = telegram.Bot(token=token)

#생성한 텔레그램 봇 정보
me = bot.getMe()
print(me)

#사용자 채널 id로 메시지 보내기
bot.sendMessage(-1001250905630, 'bot이 보낸 메시지')

# https://api.telegram.org/bot1787374542:AAHTkUuO3qKc5HlczhsNwRkhYf1pycuncIY/getUpdates 채널 주소 알아내기
# 오류가 나면 채널에 /start 입력