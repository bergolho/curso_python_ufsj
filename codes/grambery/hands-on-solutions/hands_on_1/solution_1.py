# Funcao que resolve o problema
def url_parse ( url ):
	# Quebrar a url em tokens utilizando o caracter '/' como marcador
	tokens = url.split('/')

	# Retornar o indice 2 do array de tokens ...
	return tokens[2] 

# Funcao principal em Python
def main ():
	# Ler uma string do usuario
	urlteste = raw_input ("URL = ")

	# Imprimir o retorno da funcao
	print url_parse ( urlteste )
	
if __name__ == "__main__":
	main()	


