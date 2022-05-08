'''
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
'''

def procedimiento(lista):
    for a in lista:
        print("*"*a)

procedimiento([4, 9, 7])
