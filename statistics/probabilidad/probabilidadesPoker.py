import random
import collections


Palos = ['Pica', 'Corazon', 'Diamante', 'Trebol']
Valores = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def Barajas(Palos, Valores):
    cartas = []
    for palo in Palos:
        for valor in Valores:
            cartas.append((palo, valor))
    
    return cartas

def Repartir(Baraja, NumeroCartas):
    mano = random.sample(Baraja, NumeroCartas)
    
    return mano

def Simulacion(Baraja, NumeroCartas, Intentos):
    manos =[]
    for i in range(Intentos):
        mano = Repartir(Baraja, NumeroCartas)
        manos.append(mano)
    return manos

def Pares(manos):
    resultados = []
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
    
        counter = dict(collections.Counter(valores))
        resultados.append(counter)
    
    pares = []
    for simulacion in resultados:
        for llaveContador in simulacion.keys():
            if simulacion[llaveContador] == 2:
                pares.append(llaveContador)
                break

    # for i in resultados:
    #     print(i)
    # print(pares)
    return pares

def Trio(manos):
    resultados = []
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])
    
        counter = dict(collections.Counter(valores))
        resultados.append(counter)
    
    trios = []
    for simulacion in resultados:
        for llaveContador in simulacion.keys():
            if simulacion[llaveContador] == 3:
                trios.append(llaveContador)
                break

    # for i in resultados:
    #     print(i)

    # print(trios)
    return trios

def Escalera(manos):
    resultados = []
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        valores = sorted(valores)
        resultados.append(valores)

        escalera= []
        if valores[0]-valores[4] == 4:
            escalera.append(valores)
            pass
    for i in resultados:
        print(i)
    print(escalera)
    return escalera


def Probabilidades(Juego, Intentos, NumeroCartas):
    resultado = len(Juego) / Intentos
    # print(f'La probabilidad de sacar un par en {Intentos} Juegos, de manos de {NumeroCartas} cartas es {resultado}')
    return resultado

def run(NumeroCartas, Intentos):
    mazo = Barajas(Palos, Valores)
    manos = Simulacion(mazo, NumeroCartas, Intentos)
    # pares = Pares(manos)
    # trios = Trio(manos)
    escaleras = Escalera(manos)
    probabilidad = Probabilidades(escaleras, Intentos, NumeroCartas)
    return probabilidad

if __name__ == '__main__':
    NumeroCartas = int(input('De cuantas Cartas desea que sea la mano: '))
    Intentos = int(input('cuantas veces quiere correr la simulacion: '))
    Probabilidad = run(NumeroCartas, Intentos)
    print(Probabilidad)