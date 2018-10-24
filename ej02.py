# tuplas
# lisas inmutables, no se pueden modificar 
# a partir de la v2.6 se permiten búsquedas con index
# ocupan menos espacio en memoria, son más rápidas, están más optimizadas
# claves de un diccionario
# las tuplas van entre paréntesis (además son opcionales)

a=1,2,3,4;
print(a)

b=list(a)
print(b)

c=tuple(b[1:3])
print(c)

print(7 in a)
print(a.count(2))
print(len(a))

# empaquetado de tupla
d="Juan",
print(d)
print(len(d))

# desempaquetado de tupla
fecha=2018,10,18
print(fecha)
ano,mes,dia=fecha
print(dia)
print(mes)
print(ano)