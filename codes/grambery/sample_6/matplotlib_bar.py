import numpy as np
from pylab import *

# Definindo os dados
x = [1,2,3,4,5,6]
y = [5,8,15,20,12,18]

# Plotando as barras
bar(x,y,align='center',color='#2090AA')

# Definindo os labels 
lab=("D1","D2","D3","D4","D5","D6")

# Ajustando as configuracoes do eixo x do grafico
xticks(x,lab)

# Visualizando o grafico
show()
