# biblioteca de clases y funciones

class persona():
	def __init__(self,nombre,edad,residencia):
		self.__nombre=nombre
		self.__edad=edad
		self.__residencia=residencia
	def descripcion(self):
		txt=''
		txt+=self.__nombre+' de '
		txt+=str(self.__edad)+' años y residente en ' 
		txt+=self.__residencia
		return txt

class empleado(persona):
	def __init__(self,nombre,edad,residencia,salario,inicio):
		super().__init__(nombre,edad,residencia)
		self.__salario=salario
		self.__inicio=inicio
	def descripcion(self):
		txt=super().descripcion()
		txt+=', gana '
		txt+=str(self.__salario)+'EUR y lleva en la empresa desde '
		txt+=str(self.__inicio)
		return txt

def suma(a,b):
	return a+b

def producto(a,b):
	return a*b