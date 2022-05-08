'''
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente 
todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
'''
def sum(*args):
    suma=0
    for a in args:
        suma+=a
    return suma

def multip(*args):
    producto=1
    for a in args:
        producto*=a
    return producto
    
print(sum(1,2,3,4,5))
print(multip(1,2,3,4,5))

