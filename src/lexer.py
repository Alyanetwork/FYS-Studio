# src/lexer.py

import re

KEYWORDS = {"let", "if", "else", "plot", "plot_signal", "moving_average", "rsi"}
TOKENS = {
    "NUMBER": r"\d+(\.\d+)?",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "OPERATOR": r"[+\-*/]",
    "ASSIGN": r"=",
    "LPAREN": r"\(",
    "RPAREN": r"\)",
}

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.pos = 0

    def tokenize(self):
        while self.pos < len(self.code):
            match = None
            for token_type, pattern in TOKENS.items():
                regex = re.compile(pattern)
                match = regex.match(self.code, self.pos)
                if match:
                    text = match.group(0)
                    self.tokens.append((token_type, text))
                    self.pos = match.end(0)
                    break
            if not match:
                raise SyntaxError(f"Unknown token: {self.code[self.pos]}")
        return self.tokens
