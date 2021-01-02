import re
import sys

class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokenNames = ["OPEN_PARENS", "CLOSE_PARENS", "PLUS", "MINUS", "TIMES", "DIVIDE", "NUMBER"]
        self.numOrSymbol = re.compile('(\d+|[^ 0-9])')
        self.tokens = []
        self.errors = []

    def lexer(self):
        self.tokenize = re.findall(self.numOrSymbol, self.text)
        for tok in self.tokenize:
            if tok == '(':
                self.tokens.append([tok, self.tokenNames[0]])
            elif tok == ')':
                self.tokens.append([tok, self.tokenNames[1]])
            elif tok == '+':
                self.tokens.append([tok, self.tokenNames[2]])
            elif tok == '-':
                self.tokens.append([tok, self.tokenNames[3]])
            elif tok == '*':
                self.tokens.append([tok, self.tokenNames[4]])
            elif tok == '/':
                self.tokens.append([tok, self.tokenNames[5]])
            elif tok.isnumeric() == True:
                self.tokens.append([tok, self.tokenNames[6]])
            else:
                self.errors.append(tok)
        if not self.errors:
            return self.tokens
        else:
            print("Error! Found unknown tokens.")
            print(self.errors)
            sys.exit()