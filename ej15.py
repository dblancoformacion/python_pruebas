# poo herencia

class vehiculo():
	def __init__(self,marca,modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmcarcha=False
		self.acelerando=False
		self.frenando=False
	def arranca(self):
		self.enmcarcha=True
	def para(self):
		self.enmcarcha=False
		self.acelerando=False
		self.frenando=False
	def acelera(self):
		self.acelerando=True
		self.frenando=False
	def frena(self):
		self.acelerando=False
		self.frenando=True
class coche(vehiculo):
	ruedas=4
class moto(vehiculo):
	ruedas=2
	hcaballito=False
	def caballito(self):
		self.hcaballito=True
	def arranca(self): 
		# estoy sobrescribiendo el método arrancar para que haga el caballito 
		self.enmcarcha=True
		self.hcaballito=True
class quad(moto):
	ruedas=4

a=coche('Seat','Ibiza')
b=moto('Honda','CBR')
c=quad('Quad','4x4')

print(a.marca,a.ruedas)
print(b.marca,b.ruedas)
print(c.marca,c.ruedas)

c.arranca()
print('Haciendo el caballito:',c.hcaballito)