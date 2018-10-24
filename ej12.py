# más excepciones: raise y crear excepciones propias

class ErrorPropio:
	pass

def edad(edad):
	if edad<0:
		raise TypeError('No se permiten edades negativas')
	elif edad==0:
		raise ErrorPropio('La edad no puede ser nula')
	elif edad<20:
		return 'Eres muy jóven'
	elif edad<40:
		return 'Aún eres jóven'
	elif edad<65:
		return 'Madurito'
	elif edad<100:
		return 'Cuídate...'

print(edad(0))