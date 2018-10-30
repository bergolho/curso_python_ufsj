from math import sin, exp
import numpy as np

# Funcao degrau
def Hv(x):
	# Condicao do where
	cond = x < 0
	# Usando a funcao where do NumPy
	return np.where(cond,0.0,1.0)

# Criando um array de 5 pontos igualmente espacados indo de [-1,1]
x = np.linspace( -1.0, 1.0, 5 )

# Avaliando o array 'x' na funcao f(x)
y = Hv(x)

# Imprimir os resultados
print x
print y

