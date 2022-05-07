'''
3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos 
 resulta un muy buen ejercicio.
'''

def longitud(*args):
    contador=0
    for a in args:
        contador+=1
    print("{} tiene {} elementos".format(args, contador))

longitud(1,2,3)
