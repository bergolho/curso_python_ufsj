# A funcao chamada pelo 'map' ira trabalhar em cada elemento do array
def calcula_tamanho (s):
	return len(s)

# Versao 1 da funcao maximum
def maximum (reduced,num):
	if (num > reduced):
		return num
	else:
		return reduced

# Versao 2 da funcao maximum
def maximum2 (reduced,num):
	return num if (num > reduced) else reduced

# Solucao 1: usando reduce e map
def solucao1 (lista):
	return reduce(maximum, map(calcula_tamanho,lista), 0)

# Solucao 2: usando reduce, map e lambda
def solucao2 (lista):
	return reduce(lambda r , x : x if (x > r) else r , map(calcula_tamanho,lista))	

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista = ["Lucas","Barbara","Thais","Bernardo","Ruy"]
	print lista

	result1 = solucao1(lista)
	print result1

	result2 = solucao2(lista)
	print result2
	
if __name__ == "__main__":
	main()	
