'''
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''
def operador(*args):
    suma=0
    producto=1
    for a in args:
        suma+=a
        producto*=a
    print(suma)
    print(producto)
operador(1,2,3,4,5)

#Autor: Yimmy Eman


