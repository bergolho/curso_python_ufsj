# Solucao 2 usando List Comprehension
def even_list2 (lista):
	return [ str(x) for x in lista if (x % 2 == 0) ]

# Solucao 1
def even_list (lista):
	nova_lista = []
	for x in lista:
		if (x % 2) == 0:		
			nova_lista.append( str(x) )
	return nova_lista

# Funcao principal em Python
def main ():
	lista = [2,3,6,7,8,9,10,11]
	nova_lista1 = even_list(lista)
	nova_lista2 = even_list2(lista)

	print("Lista")
	print lista
	print("Nova Lista 1")
	print nova_lista1
	print("Nova Lista 2")
	print nova_lista2	
	
if __name__ == "__main__":
	main()	


