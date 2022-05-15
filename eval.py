import os
from typing import List
from environment import *
from parser import *

from parser import SymbolToken, NumberToken, StringToken



class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))


def eval(x, env):
    "Evaluate an expression in an environment."
    if os.environ.get('DEBUG'):
        print(f"Evaluating {x}:")

    if x is None:
        return None
    elif isinstance(x, SymbolToken):      # variable reference
        return env.find(x.x)[x.x]
    elif isinstance(x, NumberToken) or isinstance(x, StringToken):  # constant literal
        return x.x # see Token class              

    # Lists from now onwards
    elif len(x) == 0:              # ()
        return None
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp    
    elif x[0] == 'if' and len(x) == 3:             # (if test conseq alt)
        (_, test, conseq) = x
        exp = (conseq if eval(test, env) else None)
        return eval(exp, env)
    elif x[0] == 'if' and len(x) == 4:             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'cond' or x[0] == 'case':  # (cond (<test> <conseq>) ...)
        for (test, conseq) in x[1:]:
            if test == 'else' or eval(test, env):
                return eval(conseq, env)
    elif x[0] == 'define':         # (define var exp)
        (_, var, exp) = x
        env[var] = eval(exp, env)
    elif x[0] == 'set!':           # (set! var exp)
        (_, var, exp) = x
        env.find(var)[var] = eval(exp, env)
    elif x[0] == 'lambda':         # (lambda (var...) body)
        (_, parms, body) = x
        return Procedure(parms, body, env)
    else:                          # (proc arg...)
        proc = eval(x[0], env)
        args = [eval(exp, env) for exp in x[1:]]

        if os.environ.get('DEBUG'):
            print("X: ", x)
            print("Proc: ", proc)
            print("Args: ", args)

        if not callable(proc):
            return proc
        return proc(*args)