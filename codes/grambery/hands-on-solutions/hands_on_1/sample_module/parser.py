# Funcao que resolve o problema
def url_parse ( url ):
	# Quebrar a url em tokens utilizando o caracter '/' como marcador
	tokens = url.split('/')

	# Retornar o indice 2 do array de tokens ...
	return tokens[2]
