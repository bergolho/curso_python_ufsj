import numpy as np

def copy_by_reference ():
	# Criando um array x
	x = np.array([ 1., 2., 3.5 ])

	# Agora o ponteiro 'a' aponta para o array 'x'
	a = x

	print "a"
	print a

	print "x"
	print x

	# Alterando o ultimo elemento de 'a'
	a[-1] = 3

	print "a"
	print a

	print "x"
	print x

def copy_by_value ():
	# Criando um array x
	x = np.array([ 1., 2., 3.5 ])


	# (sem usar ponteiro)
	# Copiando os elementos do array 'x' para 'a' 
	a = x.copy()

	print "a"
	print a

	print "x"
	print x

	# Alterando o ultimo elemento de 'a'
	a[-1] = 9

	print "a"
	print a

	print "x"
	print x

print "Copia por referencia"
copy_by_reference()

print

print "Copia por valor"
copy_by_value()




