# tests/test_lexer.py

import unittest
from src.lexer import Lexer

class TestLexer(unittest.TestCase):
    def test_tokenize(self):
        lexer = Lexer("let x = 10")
        tokens = lexer.tokenize()
        expected = [("IDENTIFIER", "let"), ("IDENTIFIER", "x"), ("ASSIGN", "="), ("NUMBER", "10")]
        self.assertEqual(tokens, expected)
