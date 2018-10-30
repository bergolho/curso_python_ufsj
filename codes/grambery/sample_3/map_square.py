def square (num):
	return num*num

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista = range(5)
	print lista

	# Usando programacao funcional com 'map'
	lista_squared = map(square, lista)
	print lista_squared	
	
if __name__ == "__main__":
	main()	
