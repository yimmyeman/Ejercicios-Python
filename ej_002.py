# Definir una función max_de_x(), que tome tres números como argumentos y devuelva el mayor de ellos.

def mayor(*args):
    mayor=args[0]
    for numero in args:
        if numero>mayor:
            mayor=numero
    return "el numero mayor es {}".format(mayor)

def menor(*args):
    menor=args[0]
    for numero in args:
        if numero<menor:
            menor=numero
    return "el numero mayor es {}".format(menor)

print(mayor(1,2,3,4,8))
print(menor(1,2,3,4,8))