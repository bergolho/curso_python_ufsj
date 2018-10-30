import math

class Ponto:
	# Construtor
	def __init__ ( self, x, y ):
		self.xCoord = x
		self.yCoord = y
	
	# Retorna valor de x	
	def getX ( self ):
		return self.xCoord

	# Retorna valor de y
	def getY ( self ):
		return self.yCoord

	# Muda a posicao do ponto (x,y) para (x+dx,y+dy)
	def shift ( self, dx, dy ):
		self.xCoord += dx
		self.yCoord += dy

	# Calcula a distancia em relacao a outro ponto 'pt'
	def distancia ( self, pt ):
		dx = self.xCoord - pt.xCoord
		dy = self.yCoord - pt.yCoord
		return math.sqrt(dx**2 + dy**2)


