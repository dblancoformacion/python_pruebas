# bucle while

import math

#n=input('¿Cuánto enteros quieres escribir? : ')

n=5

for i in range(int(n)):
	print(i,end=' ')

i=n

while i>0:
	i-=1
	print(i,end=' ')

print()
print(math.sqrt(2))
print(math.pi)
print(math.e)

#input('Pulsa enter para finalizar')