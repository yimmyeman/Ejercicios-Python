'''
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
'''

def inversa(texto):
    inverso=""
    contador=0
    for a in range(1,len(texto)+1):
        inverso+=texto[-a]
        contador+=1
        if contador==len(texto):
            return inverso

def es_palindromo(texto):
    return inversa(texto)==texto
    
print(es_palindromo("radar"))