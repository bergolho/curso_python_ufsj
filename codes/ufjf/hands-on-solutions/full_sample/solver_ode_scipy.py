# =====================================================================
# Programa que resolve uma EDO utilizando o Metodo de Euler Explicito
# Com o SciPy
# Autor: Lucas Berg
# =====================================================================
from pylab import *
from scipy.integrate import odeint

def f (u,t):
	return u

# Definir os parametros do problema
T = 3.0
u0 = 1.0
dt = 0.01
n = int(T/dt)

# Definindo os intervalos
t = np.linspace(0.0,T,n)
u = odeint(f,u0,t)

# Calculando a solucao exata
v = u0 * exp(t)

# Plotando o grafico
plot(t,v,color="r",label="Solucao exata")
plot(t,u,linestyle="--",color="b",label="Solucao aproximada")
legend(loc="best")
show()




