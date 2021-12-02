import random

def media(X):
    return sum(X) / len(X)

def var( X):
    desviacion = 0
    desviaciones = []
    desviacionesCuadradas = []
    for i in X:
        desviacion = i - media(X)
        desviaciones.append(round(desviacion, 2))
        desviacionesCuadradas.append(desviacion**2)
    return sum(desviacionesCuadradas)/len(desviacionesCuadradas), desviaciones, desviacionesCuadradas
    pass

def run(lista):
    print(f'la lista de edades es: {lista}')
    print(f'la media de edades es: {media(lista)}')
    intermedios = var(lista)
    print(f'las variaciones de edad con respecto a la media son: {intermedios[1]}')
    print(f'la varianza de edades es: {round(intermedios[0], 2)}')
    print(f'la desviacion estandar es: {round((intermedios[0]**0.5), 2)}')
    pass


if __name__ == '__main__':

    edades = [random.randint(1,40) for i in range(10)]
    run(edades)
