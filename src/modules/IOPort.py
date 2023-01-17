entrada = './IOPort/Input.txt'
saida = './IOPort/Output.txt'

def retornaArquivoEntrada():
  arquivo = open(entrada, 'r',encoding="utf-8")
  textoArquivo = arquivo.readlines()
  arquivo.close()
  return textoArquivo

def escreverArquivoSaida(conteudo):
  arquivo = open(saida, 'w')
  arquivo.writelines(conteudo)
  arquivo.close()