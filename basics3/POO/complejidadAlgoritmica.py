import time
import sys

sys.setrecursionlimit(100000)

def factorizacion(factorial):
    # print(f'n = {factorial}')
    if factorial != 1:
        respuesta = factorial*factorizacion(factorial-1)
    else: 
        respuesta = 1
    return respuesta

def factorizacion2(factorial):
    respuesta = 1

    while factorial > 1:
        respuesta *= factorial
        factorial -= 1
    
    return respuesta


def run():
    
    factorial = 20000
    
    comienzo = time.time()
    # factorial=int(input('por favor ingrese el factorial que desea obtener: '))
    respuesta = factorizacion(factorial)
    # print(f'el factorial de {factorial} es {respuesta}')
    final = time.time()
    print(f' el tiempo de ejecución del algoritmo recursivo es:{final - comienzo}')

    comienzo = time.time()
    respuesta = factorizacion2(factorial)
    # print(f'el factorial de {factorial} es {respuesta}')
    final = time.time()
    print(f' el tiempo de ejecución del algoritmo iterativo es:{final - comienzo}')


    pass


if __name__ == '__main__':
    run()