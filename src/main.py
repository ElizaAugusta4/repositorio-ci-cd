# main.py
import unittest


class test_Funcoes(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 3), 2)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b
