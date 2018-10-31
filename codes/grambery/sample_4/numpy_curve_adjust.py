import numpy as np

# Criando os vetores de dados
x = np.array([ 0.0, 1.0, 2.0, 3.0, 4.0, 5.0 ])
y = np.array([ 0.0, 0.8, 0.9, 0.1, -0.8, -1.0 ])

# Ajustando uma curva por interpolacao polinomial
# Calculando os coeficientes do polinomio de grau 1
c1 = np.polyfit(x,y,1)
print("c1") 
print(c1) 

# Avaliando o polinomio
p1 = np.poly1d(c1) 

# Calculando os coeficientes do polinomio de grau 3
c3 = np.polyfit(x,y,3)
print("c3") 
print(c3) 

# Avaliando o polinomio
p3 = np.poly1d(c3)
