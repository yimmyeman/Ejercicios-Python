#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(caracter):
    vocales=["a","e","i","o","u"]
    return caracter in vocales
print(vocal('b'))