# A funcao chamada pelo 'map' ira trabalhar em cada elemento do array
def calcula_tamanho (s):
	return len(s)

def solucao1 (lista):
	resp = []
	n = len(lista)
	for i in range(n):
		resp.append(len(lista[i]))
	return resp

def solucao2 (lista):
	return map(calcula_tamanho,lista)	

# Funcao principal em Python
def main ():
	# Criando uma lista
	lista = ["Lucas","Barbara","Thais","Bernardo","Ruy"]
	print(lista)

	r1 = solucao1(lista)
	print(r1) 

	r2 = solucao2(lista)
	print(r2) 

	# Usando programacao funcional com 'map'
	#lista_summed = map(sum, lista1, lista2)
	#print lista_summed
	
if __name__ == "__main__":
	main()	
