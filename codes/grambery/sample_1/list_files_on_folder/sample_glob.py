import os
from glob import glob

# Encontrando todos os arquivos com extensao Python
files = [f for f in glob( '*.py' )]
print(files) 

# Encontrando todos os arquivos 
files = [f for f in glob( '*' )]
print(files) 

