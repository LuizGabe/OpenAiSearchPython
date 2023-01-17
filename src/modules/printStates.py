import colorama
from colorama import Fore, Style
from modules.retornaConfig import optionData, optionBool

def printStates():
  colorama.init()
  print('')

  def imprimir(option, value):
    if value:
      print(f'{Fore.GREEN}{option}')
    else:
      print(f'{Fore.RED}{option}')

  print('Dados: ')
  for option, value in optionData.items():
    imprimir(option, value)

  print (Style.RESET_ALL)
  print('Funções: ')
  for option, value in optionBool.items():
    imprimir(option, value)
  print (Style.RESET_ALL)