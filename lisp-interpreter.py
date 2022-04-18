import argparse
import sys
from lexer import LispLexer

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
    for tok in lexer.tokenize(content):
        print('type=%r, value=%r' % (tok.type, tok.value))