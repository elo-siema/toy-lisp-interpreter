from sly import Lexer

class LispLexer(Lexer):
    # Set of token names.   This is always required
    tokens = { SYMBOL, STRING, NUMBER, COND, ELSE, DO }

    SYMBOL = r'[a-zA-Z_+=\*\-\<\>][a-zA-Z0-9_+\*\-\<\>]*'
    SYMBOL['cond'] = COND
    SYMBOL['else'] = ELSE
    SYMBOL['do'] = DO
    
    @_(r'"(.*?)"')
    def STRING(self, t):
        t.value = t.value[1:-1]
        return t

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)   # Convert to a numeric value
        return t

    literals = { '(', ')' }

    # String containing ignored characters between tokens
    ignore = ' \t'

    ignore_comment = r'\#.*'
    ignore_newline = r'\n+'

