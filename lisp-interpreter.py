import argparse
import sys
from lexer import LispLexer
from parser import LispParser
from environment import *
from eval import *

argparser = argparse.ArgumentParser(description='Lisp Interpreter')
argparser.add_argument('-f', '--file', help='File to interpret', type=argparse.FileType('r'), required=True)

args = argparser.parse_args()
lexer = LispLexer()
parser = LispParser()

if not args.file:
    # Run as REPL
    #argparser.print_usage()
    #sys.exit(-1)

with args.file as file:
    # Run file
    content = file.read()
    print("Source: ")
    print(content)
    
    tokens = lexer.tokenize(content)
    ast = parser.parse(tokens)
    print("Parsed AST: ", ast)

    result = eval(ast, standard_env())

    if result:
        print(result)