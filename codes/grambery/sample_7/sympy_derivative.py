from sympy import *

# Definindo a lista de simbolos
x = Symbol('x')

# Definindo as funcao a ser derivada
y = 2*cos(x)

# Calculando a derivada em relacao a x
dydx = diff(y,x)

# Imprimindo as funcoes
print("y")
pprint(y)

print("dydx")
pprint(dydx)
