# A funcao chamada pelo 'map' ira trabalhar em cada elemento do array
def sum (a,b):
	return a+b

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista1 = range(5)
	print lista1

	lista2 = range(10,15)
	print lista2

	# Usando programacao funcional com 'map'
	lista_summed = map(sum, lista1, lista2)
	print lista_summed
	
if __name__ == "__main__":
	main()	
