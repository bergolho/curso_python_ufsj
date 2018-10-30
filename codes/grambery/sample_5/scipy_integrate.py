import numpy as np
from scipy import integrate

# Funcao a ser integrada
def fx2 (x):
	return x*x

# Integra usando Quadratura de Gauss
def continous_integration (a,b):
	I = integrate.quad(fx2,a,b)
	print I
	return I

# Integra usando regra do Trapezio
def discrete_integration (x,y):
	I = integrate.trapz(y,dx=x[1]-x[0])
	print I
	return I	

# Integrando um intervalor continuo
I1 = continous_integration(0.0,4.0)

# Integrando um conjunto de pontos discretos
x = np.linspace(0.0,4.0,25)
y = fx2(x)
I2 = discrete_integration(x,y)
