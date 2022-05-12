import argparse
import sys
from lexer import LispLexer
from parser import LispParser
from environment import *
from eval import *

argparser = argparse.ArgumentParser(description='Lisp Interpreter')
argparser.add_argument('-f', '--file', help='File to interpret', type=argparse.FileType('r'), required=True)

args = argparser.parse_args()

if not args.file:
    argparser.print_usage()
    sys.exit(-1)

with args.file as file:
    content = file.read()
    print(content)


    lexer = LispLexer()
    tokens = lexer.tokenize(content)
    #for tok in tokens:
    #    print('type=%r, value=%r' % (tok.type, tok.value))

    parser = LispParser()
    parsed = parser.parse(tokens)
    print(parsed)

    print(eval(parsed, standard_env()))

    #while True:
    #    try:
    #        text = input('calc > ')
    #        result = parser.parse(lexer.tokenize(text))
    #        print(result)
    #    except EOFError:
    #        break
