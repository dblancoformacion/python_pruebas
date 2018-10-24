# generadores: yield from

def g_ciudades(*ciudades):
	for i in ciudades:
		for j in i:	
			yield j

def gf_ciudades(*ciudades):
	for i in ciudades:
	#	for j in i:	
			yield from i

a=gf_ciudades(
	'Santander',
	'Madrid',
	'Toledo',
	'Salamanca'
	)

for i in a:
	print(i,end='.')
