# defines the main program
from .components.parse import parse
from .components.evaluation import eval

class interpreter():
    def program(self, input):
        # A prompt-read-eval-print program.
        val = eval(parse(input))
        if val is not None:
            return self.schemestr(val)
        else:
            return ""

    def schemestr(self, exp):
        # Convert a Python object back into a Scheme-readable string.
        if isinstance(exp, list):
            return '(' + ' '.join(map(self.schemestr, exp)) + ')' 
        else:
            return str(exp)