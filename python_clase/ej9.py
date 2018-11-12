# csv

import csv
with open('ieo.txt', 'r') as csvfile:
    r = csv.reader(csvfile, delimiter=';')
    for i in r:
    	print(type(i))
    	print(i)
    	break