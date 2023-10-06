# main.py
import unittest
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b


class TestFuncoes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)
        
  