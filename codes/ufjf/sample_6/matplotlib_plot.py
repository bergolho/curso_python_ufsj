import numpy as np
from pylab import *

# Definindo o conjunto de dados a ser plotado
x = np.linspace(0,3,51)
y = x**2 * np.exp(-x**2)

# Plotando os dados
plot(x,y)

# Visualizando
show()

