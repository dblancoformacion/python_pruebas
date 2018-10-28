# poo: funcion super()

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

david=persona('David',42,'Liérganes')
ramon=empleado('Ramón',46,'Santander',1500,2016)

print(david.descripcion())
print(ramon.descripcion())

# principio de sustitución: un empleado siempre es antes persona
# sin embargo, no todas las personas son empleadas
print(isinstance(david,persona))
print(isinstance(ramon,persona))
print(isinstance(david,empleado))
print(isinstance(ramon,empleado))