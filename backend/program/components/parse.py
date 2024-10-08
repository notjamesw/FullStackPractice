from .type_definitions import *

# Converts string input into a list of tokens
# RETURNS: a list of tokens
def tokenizeProgram(chars: str) -> list:
    L = chars.replace("(", " ( ").replace(")", " ) ").split()
    return L

# Takes a string input, breaks it down into tokens, then assembles an abstract syntax tree
# RETURNS: an expression (atom or list)
def parse(input: str) -> Exp:
    return readFromTokens(tokenizeProgram(input))

# Interprets the tokens, checks if there are syntax errors, if not, generates an expression
# RETURNS: an expression
def readFromTokens(tokens: list) -> Exp:
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF')
    currToken = tokens.pop(0)
    if currToken == "(":
        L = []
        while tokens[0] != ')':
            L.append(readFromTokens(tokens))
        tokens.pop(0)
        return L
    elif currToken == ")":
        raise SyntaxError('Unexpected )')
    else:
        return atom(currToken)

# Sorts tokens into either number or symbol
# REQUIRES: Not parenthesis
# RETURNS: an atom
def atom(token: str) -> Atom:
    try:
        return int(token)
    except ValueError:
        try: 
            return float(token)
        except ValueError:
            return Symbol(token)