# excepciones

import math

def raiz(x):
	if x<0:
		raise ValueError('El número no puede ser negativo')
	else:
		return math.sqrt(x)

try:
	print(raiz(-3))
except:
	print('Error')

print('Finalizamos con normalidad')