import re
def limparTextoOuLista(lista):
    # Função auxiliar para limpar uma única string
    def limparTexto(palavra):
      # Remover caracteres de nova linha
      palavra = palavra.replace('\n', '')
      # Verificar se a string contém alguma palavra
      if palavra.strip():

        palavra = palavra.replace(':', '')
        # Junta as palavras com espaço
        palavra = ' '.join(palavra.split())
        # Verifica se existe alguma palavra alfanumerica na frase
        if not any(c.isalnum() for c in palavra):
          # Remove caracteres especiais
          palavra = re.sub(r'[^\w\s]', '', palavra)
      return palavra

    if isinstance(lista, str):
        return limparTexto(lista)
    else:
        # Usa a list comprehension para filtrar elementos vazios, nulos, com somente espaços em branco e com somente caracteres especiais
        return [string for string in map(limparTexto, lista) if string and string.strip() and any(c.isalnum() for c in string)]