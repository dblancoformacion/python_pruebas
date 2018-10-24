# poo: polimorfismo
# python es de tipado dinámico, no necesitamos especificar el tipo previamente

class coche():
	def desplazamiento(self):
		return 'Se desplaza utilizando 4 ruedas'
class moto():
	def desplazamiento(self):
		return 'Se desplaza utilizando 2 ruedas'
class camion():
	def desplazamiento(self):
		return 'Se desplaza utilizando 18 ruedas'

a=coche()
b=moto()
c=camion()
print(a.desplazamiento())
print(b.desplazamiento())
print(c.desplazamiento())

print('--- Vamos a convertir el coche en un camión ---')

def desplazamiento_vehiculo(vehiculo):
	return vehiculo.desplazamiento()

# lo que cambia de tipo es la variable vehiculo, que puede ser de tipo coche, moto o camion
# no hace falta especificar de qué tipo es la variable vehiculo
# en otros lenguajes es necesaria la herencia para explotar el polimorfismo

print(desplazamiento_vehiculo(a))
print(desplazamiento_vehiculo(c))