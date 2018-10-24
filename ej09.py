# generadores (objetos iterables)
# son más eficientes que las funciones tradicionales

def funcion(limite):
	n=1
	lista=[]
	while n<limite:
		lista.append(n*2)
		n+=1
	return lista

def generador(limite):
	n=1
	while n<limite:
		yield n*2
		n+=1

a=funcion(10)
print(a)

# ahorramos en memoria al evitar la variable lista
b=generador(10)

for i in range(3):
	print(next(b),end=' ')

print()
b=generador(10)
for i in b:
	print(i,end=' ')