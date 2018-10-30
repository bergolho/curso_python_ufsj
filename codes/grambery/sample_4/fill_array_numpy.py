import time
import numpy as np

n = 10000000
start = time.time()

a = np.arange(n)
b = np.arange(n)
c = a * b

t = time.time() - start
print("Tempo: %s" % t)
