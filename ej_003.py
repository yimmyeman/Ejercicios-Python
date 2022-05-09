'''
Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos 
 resulta un muy buen ejercicio.
'''

def longitud(*args):
    contador=0
    for a in args:
        contador+=1
    return "{} tiene {} elementos".format(args, contador)

print(longitud(1,2,3))
