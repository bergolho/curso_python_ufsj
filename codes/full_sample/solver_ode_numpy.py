# =====================================================================
# Programa que resolve uma EDO utilizando o Metodo de Euler Explicito
# Com o NumPy
# Autor: Lucas Berg
# =====================================================================
import numpy as np
from pylab import *

# Definir os parametros do problema
u0 = 1.0
T = 3.0
dt = 0.01
n = int(T/dt)

# Inicializa os vetores
u = np.zeros(n+1)
v = np.zeros(n+1)
t = np.zeros(n+1)

# Definir a condicao inicial
t[0] = 0.0
u[0] = u0

# Loop do tempo
for k in range(n):
	u[k+1] = u[k] + dt*u[k]
	t[k+1] = t[k] + dt

# Calcula solucao exata
# u(t) = u0.exp(at)
v = u0 * exp(t)

print v
print u

# Exibir o grafico da solucao
plot(t,v,color="r",label="Solucao exata")
plot(t,u,linestyle="--",color="b",label="Solucao aproximada")
legend(loc="best")
show()







