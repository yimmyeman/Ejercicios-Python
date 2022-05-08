'''
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común 
o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
'''

def superposicion(listaA,listaB):
    contador=0
    for a in listaA:
        for b in listaB:
            if a==b:
                contador+=1
    if contador>=1:
        return True
    else:
        return False
        
print(superposicion(["a","t","c","w"],["x",3,"b","r"]))

