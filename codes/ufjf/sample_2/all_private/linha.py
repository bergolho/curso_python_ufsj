from ponto import Ponto

class Linha:
	# Construtor
	def __init__ ( self, pA, pB ):
		self.__pontoA = pA # Atributo protegido
		self.__pontoB = pB # Atributo protegido
	
	# Retorna o ponto A	
	def pontoA ( self ):
		return self.__pontoA
	
	# Retorna o ponto B	
	def pontoB ( self ):
		return self.__pontoB

	# Calcula o tamanho da linha
	def comprimento ( self ):
		return self.__pontoA.distancia(self.__pontoB)

	# Calcula a distancia em relacao a outro ponto 'pt'
	def mesmoX ( self ):
		ax = self.__pontoA.getX()
		bx = self.__pontoB.getX()		
		return ax == bx


