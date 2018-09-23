# A funcao chamada pelo 'reduce' ira acumular na variavel reduced a operacao
def soma (reduced,num):
	return reduced + num*num

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista1 = range(5)
	print lista1

	# Usando programacao funcional com 'reduce' 
	# O terceiro parametro eh o valor inicial da variavel reduced
	result = reduce(soma,lista1,0)
	print result

if __name__ == "__main__":
	main()	
