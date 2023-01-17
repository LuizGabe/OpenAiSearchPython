import unittest

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src.modules.limparTextoOuLista import limparTextoOuLista

class TestLimparTextoOuLista(unittest.TestCase):
  def test_lista_vazia(self):
    self.assertEqual(limparTextoOuLista([]), [])

  def test_lista_com_somente_espacos_em_branco(self):
    self.assertEqual(limparTextoOuLista([' ', '\t', '\n']), [])

  def test_lista_com_somente_caracteres_especiais(self):
    self.assertEqual(limparTextoOuLista(['!', '@', '#']), [])

  def test_lista_com_elementos_validos(self):
    self.assertEqual(limparTextoOuLista(['\tHello World!\n', '\nPython    is    fun\n']), ['Hello World!', 'Python is fun'])

  def test_entrada_string(self):
    self.assertEqual(limparTextoOuLista('\tHello World!\n'), 'Hello World!')

  def test_entrada_string_com_espaco(self):
    self.assertEqual(limparTextoOuLista(' '), ' ')

  def test_entrada_string_com_caractere_especial(self):
    self.assertEqual(limparTextoOuLista('#'), '')

  def test_entrada_string_comecado_dois_pontos(self):
    self.assertEqual(limparTextoOuLista(':A fotossintese'), 'A fotossintese')

if __name__ == '__main__':
  unittest.main()