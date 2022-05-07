'''
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" 
debería devolver la cadena "odnaborp yotse"
'''
def invertir(texto):
    for a in range(1,len(texto)+1):
        print(texto[-a], end="")
invertir("Hola Mundo")