from LexicalAnalyzer import Lexer
from ShiftReduceParser import Parser
import pprint


equation = " -4+(10/5)*3"
lexer = Lexer(equation)
tokens = lexer.lexer()
print("LEXICAL ANALYSIS OUTPUT:")
pprint.pprint(tokens)
print("\n")

print("SYNTAX ANALYSIS OUTPUT:")
parser = Parser(tokens)
syntaxAnalysis = parser.parser()
answer = eval(equation)
print("The answer is: " + str(answer))

# (1  + 2 ) * (3 / (5*4)) +   (10 / 5)
# 1  + 2 +   (10 / 5)

