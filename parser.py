from sly import Parser
from lexer import LispLexer

class LispParser(Parser):
    # Get the token list from the lexer (required)
    tokens = LispLexer.tokens
    debugfile = 'parser.out'

    @_('expr seq')
    def seq(self, p):
        return ('seq', [p.expr, p.seq] if p.seq else [p.expr])

    
    # Grammar rules and actions
    @_('SYMBOL',
       'STRING',
       'NUMBER',
       'COND',
        'ELSE',
        'DO',
       'list_'
       )
    def expr(self, p):
        return ('expr', p[0])

    @_('"(" seq ")"')
    def list_(self, p):
        return ('list', p.seq)

    @_('')
    def seq(self, p):
        pass