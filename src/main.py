# Library Imports
from tqdm import tqdm
import asyncio

# Module Imports
from modules.retornaConfig import sendMessage, sendDocx, createDocx , nome, dataAtual
from modules.IOPort import escreverArquivoSaida, retornaArquivoEntrada
from modules.telegramBot import telegramMessage, telegramDocument
from modules.limparTextoOuLista import limparTextoOuLista
from modules.printStates import printStates
from modules.openAi import pesquisar
from modules.criarDocx import *

pesquisaLimpa =  limparTextoOuLista(retornaArquivoEntrada())
conteudoSoRespostas = []

async def main():
  for i in tqdm(range(5)):
    pesquisa = pesquisaLimpa[i]
    retorno = await pesquisar(pesquisa)

    textoRetornado = retorno["choices"][0]["text"]

    # Arrumando o resultado obtido
    textoRetornadoLimpo = limparTextoOuLista(textoRetornado).capitalize()

    # Guardar somente respostas em uma lista
    conteudoSoRespostas.append(textoRetornadoLimpo)

  saidaOutput = [f'{pesquisa}\n{resposta}\n\n' for (pesquisa, resposta) in zip(pesquisaLimpa, conteudoSoRespostas)]
  saidaTelegram = [f'<b>{pesquisa}</b>\n{resposta}\n\n' for (pesquisa, resposta) in zip(pesquisaLimpa, conteudoSoRespostas)]
  saidaDocx = [f'{pesquisa}\n{resposta}' for (pesquisa, resposta) in zip(pesquisaLimpa, conteudoSoRespostas)]


  escreverArquivoSaida(saidaOutput)

  if sendMessage:
    await telegramMessage(''.join(saidaTelegram))
  
  if createDocx:
    adicionarCabecalho('Nome: ', nome)
    adicionarCabecalho('Data: ', dataAtual)
    adicionarConteudo('')
    for junta in saidaDocx:
      pergunta, resposta = junta.split('\n')
      adicionarTitulo(pergunta)
      adicionarConteudo(resposta)
      adicionarConteudo('')
    configAndSave()

  if sendDocx:
    if createDocx:
      await telegramDocument(pathDocumentSave)
    else:
      print('Você não pode enviar um arquivo que não criou. :(')

printStates()
asyncio.run(main())