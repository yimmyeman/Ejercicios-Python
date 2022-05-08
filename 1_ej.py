'''
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy 
buen ejercicio.
'''

def numero_maximo(a, b):
    if a>b:
        return "EL numero mayor es {}".format(a)
    elif a==b:
        return "{} y {} son iguales".format(a,b)
    else:
        return "EL numero mayor es {}".format(b)

print(numero_maximo(2, 3))