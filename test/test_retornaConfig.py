import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from src.modules.retornaConfig import *

class TestConfigFile(unittest.TestCase):
    def test_apiKeyOpenai(self):
        self.assertTrue(apiKeyOpenai.strip())
        
    def test_tokenBotFather(self):
        self.assertTrue(tokenBotFather.strip())
        
    def test_myChatTelegram(self):
        self.assertTrue(myChatTelegram.strip())
        
    def test_nome(self):
        self.assertTrue(nome.strip())

if __name__ == '__main__':
    unittest.main()
