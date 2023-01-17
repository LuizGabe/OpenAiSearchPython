from modules.IOPort import retornaArquivoEntrada, escreverArquivoSaida
from modules.limparTextoOuLista import limparTextoOuLista
from modules.openAi import pesquisar
import asyncio

stringLimpa = limparTextoOuLista(retornaArquivoEntrada())
print(pesquisar(stringLimpa))