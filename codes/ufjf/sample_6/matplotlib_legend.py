import numpy as np
from pylab import *

# Primeira curva
x = np.linspace(-6,6,500)
plot(x,sin(x),label="sin(x)")

# Segunda curva
plot(x,cos(x),label="cos(x)")

# Informacoes do grafico
title("Seno e Cosseno")
xlabel("x")
ylabel("f(x)")

# Definindo os limites do plot
axis([-6,6,-2,2])

# Adicionando a legenda no canto superior direito
#legend(loc="upper right")
# Adicionando a legenda no canto superior esquerdo
#legend(loc="upper left")
# Adicionando a legenda na melhor posicao possivel
legend(loc="best")

# Visualizando o grafico
show()

