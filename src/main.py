from modules.IOPort import retornaArquivoEntrada, escreverArquivoSaida
from modules.retornaConfig import nome, dataAtual
from modules.limparTextoOuLista import limparTextoOuLista
from modules.criarDocx import *
from modules.telegramBot import telegramMessage
from modules.printStates import printStates
from modules.openAi import pesquisar
import asyncio

stringLimpa = limparTextoOuLista(retornaArquivoEntrada())
retorno = asyncio.run(pesquisar(stringLimpa))
print(retorno)
asyncio.run(telegramMessage(retorno))
printStates()

adicionarCabecalho('Nome: ', nome)
adicionarCabecalho('Data: ', dataAtual)
adicionarConteudo('')
adicionarTitulo(stringLimpa)
adicionarConteudo(retorno)
configAndSave()