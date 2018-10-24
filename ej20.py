# modularidad: uso de ej19.py

import ej19
from ej19 import suma
from ej19 import *

from ej16 import persona

print(ej19.suma(1,2))
print(ej19.producto(3,4))

print(suma(4,7))
print(producto(3,4))

a=persona('David',40,'Solares')
print(a.descripcion())

#ramon=empleado('Ramón',46,'Santander',1500,2016)