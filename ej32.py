# db: mysql
import pip
pip.main(['install','mysql-connector-python-rf'])
#import mysql.connector
from mysql.connector import (connection)
#conn=mysql.connector.connect(
conn=connection.MySQLConnection(
	host='',
	user='',
	password='',
	database='redya_es_curso'
	)
rs=conn.cursor()
rs.execute('''
	SELECT * FROM equipos;
	''')
r=rs.fethcall()
for i in r:
	print(r)
conn.close()