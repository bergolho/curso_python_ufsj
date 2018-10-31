from ponto import Ponto

# Funcao principal em Python
def main ():
	p1 = Ponto(5.0, 7.0)
	p2 = Ponto(0.0, 0.0)

	x = p1.getX()
	y = p1.getY()	
	
	print( "(" + str(x) + ", " + str(y) + ")" )
	
	p2.shift(4.0,12.0)
	d = p1.distancia(p2)
	print("Distancia = ", d)	
	
if __name__ == "__main__":
	main()	
