def make_incrementer (n):
	return lambda x: x + n

# Funcao principal em Python
def main ():

	# Usando programacao funcional com 'lambda'
	# Definindo uma funcao que realiza o incremento de 2 
	f = make_incrementer(2)
	# Definindo uma funcao que realiza o incremento de 6 
	g = make_incrementer(6)

	print(f(42), g(42)) 

if __name__ == "__main__":
	main()	
