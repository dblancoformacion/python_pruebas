# db local

import mysql.connector

def cuadro(ancho,texto):
	if not ancho: ancho=70
	margen_i=round((ancho-2-len(texto))/2)
	margen_d=ancho-margen_i-len(texto)
	txt='╔'
	for i in range(ancho):
		txt+='═'
	txt+='╗\n'
	txt+='║'
	for i in range(margen_i): txt+=' '
	txt+=texto
	for i in range(margen_d): txt+=' '
	txt+='║\n'
	txt+='╚'
	for i in range(ancho): txt+='═'
	txt+='╝\n'
	return txt

conn = mysql.connector.connect(
	host='172.31.128.235',
	user='oceanografico',
	password='lamar',
	database='oceano'
)

rs=conn.cursor()
rs.execute("""
	SELECT * FROM usuarios;
	""")
r=rs.fetchall()
print(cuadro(60,'Usuarios autentificados del sistema'))
for i in r:
	print(i[1])

input()