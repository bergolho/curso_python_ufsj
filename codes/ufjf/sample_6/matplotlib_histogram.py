import numpy as np
from pylab import *

# Criando um conjunto aleatorio de amostras
y = np.random.randn(1000)

# Plotando os dados por um histograma
hist(y,bins=50)

# Visualizando
show()
