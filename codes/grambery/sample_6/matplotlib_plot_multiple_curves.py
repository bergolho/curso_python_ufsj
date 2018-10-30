import numpy as np
from pylab import *

# Primeira curva
y = np.linspace(-3,3,10)
plot(y)

# Segunda curva
x = np.linspace(0,9,100)
plot(x,sin(x))

# Terceira curva vermelha e tracejada
plot(x,cos(x), linestyle="--", color="r")

# Quarta curva magenta e tracejada com pontos
plot(x,exp(sin(x)), linestyle="-.", color="m") 

# Adicionando linhas de grade
grid()

# Visualizando o grafico
show()

