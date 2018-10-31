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
	# Quebrando uma string usando os ' ' como marcadores
	txt = "There is someone in my head".split()

	# Criando uma lista de tuplas em que
	# Primeiro elemento sera todo escrito em uppercase
	# Segundo elemento sera todo escrito em lowercase	
	# Terceiro elemento e o numero de caracteres do token	
	nova = [(p.upper(),p.lower(),len(p)) for p in txt]
	print(nova)	
	
if __name__ == "__main__":
	main()	


