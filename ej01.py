# ej1

def suma(a,b):
	a=3
	b=4
	return(a+b)

def mensaje():
	print("Hola Mundo")
	print("Adios Mundo")

a=[	'login','hola','adios',3.1,'hola']
a.append('final');
a.insert(2,'insertado')
a.extend(['este','otro' ])
print(a.index('otro'))
print(3.1 in a)
#a.remove('hola')
#a.remove('hola')
a.pop()

print(a[:])

b=['Sandra','Lucía']
a.extend(b)
a=a+b
a+=b
print(a)
a=[1,2,3,4]
print(a*2)


# https://www.youtube.com/watch?v=vawEHhV_HFA&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=6