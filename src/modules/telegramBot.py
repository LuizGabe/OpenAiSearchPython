from modules.retornaConfig import myChatTelegram, tokenBotFather
import telegram

bot = telegram.Bot(token=tokenBotFather)

async def telegramMessage(text):
  await bot.send_message(
    chat_id=myChatTelegram,
    text=text, 
    parse_mode='HTML'
  )

async def telegramDocument(path):
  await bot.sendDocument(
    chat_id=myChatTelegram, 
    document=open(path, 'rb')
  )