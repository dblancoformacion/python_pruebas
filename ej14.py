# poo

class Coche():
	# propiedades
	largo=250
	ancho=120
	__ruedas=4 # privada, no accesible desde fuera ENCAPSULACIÓN
	aceite=True
	enmarcha=False
	# metodos
	def __init__(self): # constructor
		pass
	def __chequeo(self):
		ok=True
		if self.__ruedas!=4 :
			ok=False
		if not self.aceite:
			ok=False
		return ok
	def arranca(self):
		if self.__chequeo():
			self.enmarcha=True
	def para(self):
		self.enmarcha=False
	def ruedas(self):
		return self.__ruedas
		
#instanciación de clase
a=Coche()
b=Coche()
a.arranca()
b.aceite=False
b.arranca()
#print('Chequeo del coche 2: ',b.__chequeo())
#a.__ruedas=5 # da error
print('Coche 1 en marcha: ',a.enmarcha)
print('Coche 2 en marcha: ',b.enmarcha)
print('Ruedas del coche 1: ',a.ruedas())