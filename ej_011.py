# Crea una función mcd() para calcular el máximo común divisor de varios números:

def mcd(*args):
    divisores=[]
    for x in range(len(args)):
        for i in range (1, args[x]+1):
            if args[x] % i == 0:
                divisores.append(i)
    divisores_comunes=[]
    for element in divisores:
        if divisores.count(element) == len(args):
            divisores_comunes.append(element)
    mcd=max(divisores_comunes)
    return int(mcd)