# src/interpreter.py

from parser import Parser
from lexer import Lexer

class Interpreter:
    def __init__(self, code):
        self.code = code
        self.variables = {}

    def execute(self):
        lexer = Lexer(self.code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()

        for expr in ast:
            if isinstance(expr, float):
                print(f"Number: {expr}")
            elif expr in self.variables:
                print(f"Variable: {self.variables[expr]}")
            else:
                print("Unknown expression")
