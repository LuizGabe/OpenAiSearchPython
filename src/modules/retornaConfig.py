from datetime import datetime
import json
import os

pathConfig = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/config.json'))
pathConfigCopy = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../config/config copy.json'))

try:
  jsonConfig = json.load(open(pathConfig, "r"))

  if not jsonConfig['API_KEY_OPENAI'].strip():
    jsonConfig = json.load(open(pathConfigCopy, "r"))

except:
  print('Ocorreu Um Erro')

apiKeyOpenai = jsonConfig['API_KEY_OPENAI']
tokenBotFather = jsonConfig['TOKEN_BOTFATHER']

sendMessage = jsonConfig['SEND_MESSAGE']
createDocx = jsonConfig['CRIAR_DOCX']
sendDocx = jsonConfig['SEND_DOCX']

optionData = {}
optionBool = {}

for key, value in jsonConfig.items():
  if not value in ['', ' ']:
    optionData[key] = True
  else:
    optionData[key] = False

for key, value in jsonConfig.items():
  if isinstance(value, bool):
    optionBool[key] = value

myChatTelegram = jsonConfig['YOUR_CHAT_ID']
nome = jsonConfig['NOME']
dataAtual = datetime.today().strftime(f'%d/%m/%Y')