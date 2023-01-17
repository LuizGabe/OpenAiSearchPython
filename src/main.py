from modules.IOPort import retornaArquivoEntrada, escreverArquivoSaida
from modules.openAi import pesquisar
import asyncio

print(asyncio.run(pesquisar('Fotossintese')))