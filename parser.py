from sly import Parser
from lexer import LispLexer

class Token():
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return str(self.x)

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.x == other.x
        elif isinstance(other, str):
            return self.x == other

    def __hash__(self):
        return hash(self.x)

class StringToken(Token):
    pass

class NumberToken(Token):
    pass

class SymbolToken(Token):
    pass

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

    @_('SYMBOL')
    def expr(self, p):
        return SymbolToken(p[0])
    
    @_('STRING')
    def expr(self, p):
        return StringToken(p[0])

    @_('NUMBER')
    def expr(self, p):
        return NumberToken(p[0])

    @_('list_')
    def expr(self, p):
        return p[0]

    @_('"(" seq ")"')
    def list_(self, p):
        return p.seq
