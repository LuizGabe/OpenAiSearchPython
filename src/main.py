from modules.IOPort import retornaArquivoEntrada, escreverArquivoSaida
from modules.limparTextoOuLista import limparTextoOuLista
from modules.telegramBot import telegramMessage
from modules.openAi import pesquisar
import asyncio

stringLimpa = limparTextoOuLista(retornaArquivoEntrada())
retorno = asyncio.run(pesquisar(stringLimpa))
print(retorno)
asyncio.run(telegramMessage(retorno))
