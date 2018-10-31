from parser import url_parse

# Funcao principal em Python
def main ():

	# Chamar a funcao 'url_parse' do modulo parser
	a = url_parse( "http://www.ufjf.br/deptocomputacao/sou-aluno/plano-departamental/" )
	print(a) 
	
if __name__ == "__main__":
	main()	


