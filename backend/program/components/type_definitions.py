from typing import Union
Symbol = str                    # A Scheme Symbol is implemented as a Python str
Number = Union[int, float]      # A Scheme Number is implemented as a Python int or float
Atom   = Union[Symbol, Number]  # A Scheme Atom is a Symbol or Number
List   = list                   # A Scheme List is implemented as a Python list
Exp    = Union[Atom, List]      # A Scheme expression is an Atom or List
Env    = dict                   # A Scheme environment (defined below) 
                                # is a mapping of {variable: value}
