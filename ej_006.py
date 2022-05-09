'''
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"
'''
def inversa(texto):
    inverso=""
    contador=0
    for a in range(1,len(texto)+1):
        inverso+=texto[-a]
        contador+=1
        if contador==len(texto):
            return inverso

#print(inversa("Hola Mundo"))