# Solucao 2 usando List Comprehension
def power_list2 (lista):
	return [ x*x for x in lista ]

# Solucao 1
def power_list (lista):
	nova_lista = []
	for x in lista:
		nova_lista.append(x*x)
	return nova_lista

# Funcao principal em Python
def main ():
	lista = [2,4,6,8,10]
	nova_lista1 = power_list(lista)
	nova_lista2 = power_list2(lista)

	print("Lista")
	print lista
	print("Nova Lista 1")
	print nova_lista1
	print("Nova Lista 2")
	print nova_lista2	
	
if __name__ == "__main__":
	main()	


