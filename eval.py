
from typing import List
from environment import *
from parser import *

from parser import *


class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))



def eval(x, env):
    #print(f"Evaling {x}:")
    "Evaluate an expression in an environment."
    if x is None:
        return None
    elif isinstance(x, SymbolToken):      # variable reference
        return env.find(x.x)[x.x]
    elif isinstance(x, NumberToken) or isinstance(x, StringToken):  # constant literal
        return x.x #assume Token type                
    elif x[0] == 'quote':          # (quote exp)
        (_, exp) = x
        return exp
    elif x[0] == 'if':             # (if test conseq alt)
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
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
        #print("X: ", x)
        #print("Proc: ", proc)
        #print("Args: ", args)
        if not callable(proc):
            return proc
        return proc(*args)