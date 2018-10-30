from math import sin, exp
import numpy as np

# Usando as funcoes do NumPy
def f(x):
	return np.exp(np.sin(x))

# Criando um array de 100 pontos igualmente espacados indo de [0,6]
x = np.linspace( 0.0, 6.0, 100 )

# Avaliando o array 'x' na funcao f(x)
y = f(x)

# Imprimir os resultados
print x
print y

