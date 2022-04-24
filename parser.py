from sly import Parser
from lexer import LispLexer

class LispParser(Parser):
    # Get the token list from the lexer (required)
    tokens = LispLexer.tokens
    debugfile = 'parser.out'

    # Grammar rules and actions
    @_('expr seq')
    def seq(self, p):
        return [p.expr, *p.seq] if p.seq else [p.expr]
    
    @_('')
    def seq(self, p):
        pass

    @_('SYMBOL',
       'STRING',
       'NUMBER',
       'list_'
       )
    def expr(self, p):
        return p[0]

    @_('"(" seq ")"')
    def list_(self, p):
        return p.seq
