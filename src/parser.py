# src/parser.py

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse_expression(self):
        token = self.tokens[self.pos]
        if token[0] == "NUMBER":
            return float(token[1])
        elif token[0] == "IDENTIFIER":
            return token[1]
        else:
            raise SyntaxError("Invalid syntax in expression")

    def parse(self):
        ast = []
        while self.pos < len(self.tokens):
            expr = self.parse_expression()
            ast.append(expr)
            self.pos += 1
        return ast
