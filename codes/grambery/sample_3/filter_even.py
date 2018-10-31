# A funcao chamada pelo 'filter' ira verificar o predicado(condicao) em cada elemento do array
def is_even (num):
	return num % 2 == 0

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista1 = list(range(5))
	print(lista1) 

	# Usando programacao funcional com 'filter'
	lista1_even = list(filter(is_even,lista1))
	print(lista1_even) 	

if __name__ == "__main__":
	main()	
