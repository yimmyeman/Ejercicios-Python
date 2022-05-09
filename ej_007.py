'''
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
'''
from ej_006 import inversa

def es_palindromo(texto):
    return inversa(texto)==texto
    
print(es_palindromo("radar"))