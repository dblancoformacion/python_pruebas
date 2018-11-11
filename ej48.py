# termostato

import mysql.connector

conn = mysql.connector.connect(
	host='192.168.1.51',
	user='python',
	password='python',
	database='db2017',
)
rs=conn.cursor()
rs.execute("""
	SELECT * FROM temperaturas ORDER BY id DESC LIMIT 1;
	""")
r=rs.fetchall()
for i in r:
	print(i[1])
