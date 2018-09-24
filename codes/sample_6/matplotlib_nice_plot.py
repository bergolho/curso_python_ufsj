import numpy as np
from pylab import *

# Definindo o conjunto de dados a ser plotado
x = np.linspace(0,3,51)
y = x**2 * np.exp(-x**2)

# Titulo do eixo x
xlabel("x")
# Titulo do eixo y
ylabel("f(x)")
# Titulo do grafico
title("Exemplo")
# Adicionando linhas de grade
grid()
# Plotando os dados
plot(x,y)

# Visualizando o grafico
show()

