# Solucao 1
def somaCumulativa ( l ):
	# Calcular o tamanho da lista
	n = len(l)

	# Criar uma lista com 'n' elementos
	r = range(n)

	# Inicializar o acumulador
	sum = 0
	
	# Iterar ao longo da lista 'l' e salvar a soma acumulada na lista 'r'
	for i in range(n):
		sum = sum + l[i]
		r[i] = sum

	# Retornar a lista da soma cumulativa
	return r	

# Solucao 2
def somaCumulativa2 ( l ):
	# Criar uma lista vazia
	r = []

	# Inicializar o acumulador
	sum = 0
	
	# Iterar ao longo da lista 'l' e salvar a soma acumulada na lista 'r'
	for i in range(len(l)):
		sum = sum + l[i]		
		# Adicionar o valor atual do acumulador no final da lista
		r.append(sum)

	# Retornar a lista da soma cumulativa
	return r

# Funcao principal em Python
def main ():
	# Definindo uma lista de inteiros
	l = [1,2,3,4]

	# Calcular o lista com a soma cumulativa 
	r = somaCumulativa(l)
	#r = somaCumulativa2(l)

	# Imprimir a lista
	print r
	
if __name__ == "__main__":
	main()	


