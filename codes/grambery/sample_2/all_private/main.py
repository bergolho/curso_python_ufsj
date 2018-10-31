from ponto import Ponto
from linha import Linha

# Funcao principal em Python
def main ():
	p1 = Ponto(1.0, 1.0)
	p2 = Ponto(0.0, 0.0)
	print(p1)
	print(p2) 

	x = p1.getX()
	y = p1.getY()	
	
	print( "(" + str(x) + ", " + str(y) + ")" )
	
	d = p1.distancia(p2)
	print("Distancia = ", d) 	
	
	p2.shift(1.0,1.0)
	if p1 == p2:
		print("Os pontos sao iguais") 
	

	l1 = Linha(p1,p2)
	c = l1.comprimento()
	print("Comprimento = ", c) 
	
if __name__ == "__main__":
	main()	
