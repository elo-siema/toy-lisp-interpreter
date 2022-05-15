import argparse
import sys
from lexer import LispLexer
from parser import LispParser
from environment import *
from eval import *

argparser = argparse.ArgumentParser(description='Lisp Interpreter')
argparser.add_argument('-f', '--file', help='File to interpret', type=argparse.FileType('r'))

args = argparser.parse_args()
lexer = LispLexer()
parser = LispParser()

def repl():
    env = standard_env()
    prompt = "> "
    content = ""
    while True:
        try:
            content += input(prompt)
            tokens = lexer.tokenize(content)
            ast = parser.parse(tokens)
            val = eval(ast, env)
            if val is not None: 
                print(prettyprint(val))
        except EOFError:
            # multiline input
            prompt = ''
            continue
        except Exception as ex:
            # eval error / syntax error
            print(ex)
        except KeyboardInterrupt:
            # cancel multiline input
            if prompt == "":
                print()
            else:
                raise

        content = ""
        prompt = "> "


def prettyprint(exp):
    if isinstance(exp, List):
        return '(' + ' '.join(map(prettyprint, exp)) + ')' 
    else:
        return str(exp)

def eval_file(file):
    with args.file as file:
        content = file.read()
        print("Source: ")
        print(content)

        tokens = lexer.tokenize(content)
        ast = parser.parse(tokens)
        print("Parsed AST: ", ast)

        result = eval(ast, standard_env())

        if result:
            print(prettyprint(result))


if not args.file:
    # Run as REPL
    repl()
    exit()
else:
    # Run file
    eval_file(args.file)