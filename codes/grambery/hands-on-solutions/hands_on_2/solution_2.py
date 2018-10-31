from ponto import Ponto

def le_pontos (arquivo):
	# Cria uma lista de Pontos vazio
	pts = []

	# Abre o arquivo de entrada
	infile = open(arquivo,"r")

	# Ler o numero de pontos e o converte para inteiro
	line = infile.readline()
	n = int(line)

	# Ler cada um dos pontos do arquivo
	for i in range(n):
		# Ler a linha
		line = infile.readline()
		# Quebrar em tokens usando o ' ' como marcador
		tokens = line.split()
		# Criar um objeto do tipo Ponto e adicionar na lista
		pts.append( Ponto(float(tokens[0]),float(tokens[1])) )
		
	# Fecha o arquivo
	infile.close()

	# Retorna a lista
	return pts

# Funcao principal em Python
def main ():
	arquivo = "pontos.txt"
	pts = le_pontos(arquivo)
	for pt in pts:
		print(pt) 
	
if __name__ == "__main__":
	main()	
