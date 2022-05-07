# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def numero_maximo(a,b,c):
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    mayor=lista[0]
    for numero in lista:
        if numero>mayor:
            mayor=numero
    print("el numero mayor es {}".format(mayor))
    

def numero_minimo(a,b,c):
    lista=[]
    lista.append(a)
    lista.append(b)
    lista.append(c)
    menor=lista[0]
    for numero in lista:
        if numero<menor:
            menor=numero
    print("el numero menor es {}".format(menor))
    

numero_maximo(2,5,5)
numero_minimo(2,5,5)


#varios numeros:
def mayor(*args):
    mayor=args[0]
    for numero in args:
        if numero>mayor:
            mayor=numero
    print("el numero mayor es {}".format(mayor))

def menor(*args):
    menor=args[0]
    for numero in args:
        if numero<menor:
            menor=numero
    print("el numero mayor es {}".format(menor))

mayor(1,2,3,4,8)
menor(1,2,3,4,8)