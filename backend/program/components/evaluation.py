from .environments import standard_env
from .type_definitions import *

# Evaluates an expression in the defined environment
# REQUIRES: x is an expression
def eval(x, env=standard_env()) -> Exp:
    if isinstance(x, Symbol):       # variable reference
        return env[x]
    elif isinstance(x, Number):     # number constant
        return x
    elif x[0] == "if":               # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == "define":           # defining a variable
        (_, symbol, exp) = x
        env[symbol] = eval(exp, env)
    else:                            # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)

