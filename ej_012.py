# Crea una función mcm() para calcular el mínimo común múltiplo de varios números:

#importamos la función mcd()
from ej_011 import *
def mcm(*args):
	valor=1
	for x in range(len(args)):
		valor=valor*args[x]
	numero = valor / mcd(*args)
	return int(numero)
	
print(mcm(12,15,24))

