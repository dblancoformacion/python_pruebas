# excepciones: errores en tiempo de ejecución (sin errores de sintaxis)

#op1=12

while True:
	try: # requiere except o finally (al menos una)
		op1=float(input('Introduce un denominador al numerador 12: '))
		print(12/op1)
		break
	except ZeroDivisionError:
		print('No puedo dividir por 0')
	except TypeError:
		print('Tipo de dato no válido')
	except: # excepción genérica
		print('Error inesperado')
	finally:
		print('Esto se ejecuta sí o sí')

print('Termino con éxito')
input()