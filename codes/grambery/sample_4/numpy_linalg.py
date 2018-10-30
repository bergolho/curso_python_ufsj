import numpy as np
import numpy.linalg as linalg

# Criando uma matriz A
A = np.matrix([[ 3., 2., 4. ],  
		[ 1., 1., 2. ],
		[ 4., 3., -2. ]])
print "A"
print A

# Criando o vetor coluna b
b = np.matrix([ [1.], [2.], [3.] ])

print "b"
print b

# Resolvend o sistema linear
x = linalg.solve(A,b)

print "x"
print x

