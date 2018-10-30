from sympy import *

# Definindo a lista de simbolos
x = Symbol('x')

# Calculando o limite fundamental
a = limit(sin(x)/x, x, 0)
print a

# Calculando o limite da expressao
b = limit(1/x, x, oo)
print b 

