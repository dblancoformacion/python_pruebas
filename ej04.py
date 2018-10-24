# control de flujo: condicionales y bucles

print('Programa de evaluación de alumnos')

# para que funcione input hay que ir a tools->REPL->Python->Run current file
nota_alumno=int(input('Introduce una nota numérica: '))
#nota_alumno=6;

def nota(nota):
	n='aprobado'
	if nota<5:
		n='suspenso'
	else:
		if nota>8:
			n='sobresaliente'
	return n

print(nota(nota_alumno))

input('Pulsa enter tecla para cerrar')