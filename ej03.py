# diccionarios
# asociación de tipo clave:valor (array asociativo o hash table)

a={
	'login':'david',
	'passwd':'tecla',
	'color':'verde',
}

print(a)
print(a['passwd'])

a['altura']=176
a['peso']=85
a['asistencia']=[1,2,3,4]

print(a)
print(len(a))

del a['color']
print(a)

print(a.keys())
print(a.values())
print(len(a))