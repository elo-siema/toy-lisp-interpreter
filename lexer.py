from sly import Lexer

class LispLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { SYMBOL, STRING, NUMBER, LPAREN, RPAREN }

    SYMBOL = r'[a-zA-Z_+=\*\-\<\>][a-zA-Z0-9_+\*\-\<\>]*'
    STRING = r'\"[a-zA-Z0-9_+\*\- :,]*\"'
    NUMBER = r'\d+'
    LPAREN = r'\('
    RPAREN = r'\)'

    # String containing ignored characters between tokens
    ignore = ' \t'

    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

