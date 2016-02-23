import sys
import ply.lex as lex
import ply.yacc as yacc


import decaflexer
import decafparser
linesum = []

testmode = "debug"
#testmode = "release"
filename = ""
inputstring = ""

lexer = lex.lex(module=decaflexer)
if testmode == "debug":
    filename = "input.txt"
else :
    filename = sys.argv[1]
        
f = open(filename)
rin = f.readlines()
for i in range(0, len(rin)):
    inputstring += rin[i]
    linesum.append(len(rin[i]))
    if i != 0 :
        linesum[i] += linesum[i - 1]
for i in range(len(rin) - 1, 0, -1) :
    linesum[i] = linesum[i - 1]

lexer.input(inputstring)
for token in lexer:
    print token
myparser = yacc.yacc(module=decafparser)
result = myparser.parse(inputstring)
if result == "Correct!" :  
    print(result)
