import numpy as np
from pylab import *

# Definindo os dados
x = np.linspace(-3,3,1000)
y = sin(1/x)

# Plotando o grafico
plot(x,y)

# Salvando a figura 
# Argumentos: (nomedoarquivo,formato)
savefig("seno1sx",format="pdf")


