# bucles i

j=0
a=range(5)

print(a)

for i in a:
	print('Hola',end=' ')	# elimina el salto de línea

for i in 'dblanco@alpeformacion.es':
	print(i,end=' ')
	if i=='@' or i=='.':
		j+=1

print()

if j==2:
	print('email válido')
else:
	print('email no válido')

print('')