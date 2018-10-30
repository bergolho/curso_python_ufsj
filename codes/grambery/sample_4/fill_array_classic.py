import time

n = 10000000
start = time.time()

a, b = range(n), range(n)
c = []

for i in a:
	c.append(a[i] * b[i])

t = time.time() - start
print("Tempo: %s" % t)

