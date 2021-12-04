import random
import collections


Palos = ['Pica', 'Corazon', 'Diamante', 'Trebol']
Valores = ['As','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','J','Q','K' ]

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

def escalera(manos):
    resultados = []
    for mano in manos:
        mano_ordenada = []
        for posicion in Valores:
            for valor in mano:
                if posicion == valor:
                    mano_ordenada.append(posicion)
                
        start = -1
        for valor in mano_ordenada:
                if start == -1:
                    for i in range(len(Valores)):
                        if valor == Valores[i]:
                            start=i
                            break

                valores_concecutivos=0
                concecutivo=True
                i=0
        for valor in mano_ordenada:    
            if concecutivo == True:
                for posicion in Valores[start+i:]:
                    if valor == posicion:
                        valores_concecutivos+=1
                        i+=1
                        break
                    else:
                        concecutivo=False
                        break
            
            if valores_concecutivos == 5:
                resultados.append(mano_ordenada)
    ganadora = ['As','dos','tres','cuatro','cinco']
    resultados.append(ganadora)
    return resultados


def Probabilidades(Juego, Intentos, NumeroCartas):
    resultado = len(Juego) / Intentos
    # print(f'La probabilidad de sacar un par en {Intentos} Juegos, de manos de {NumeroCartas} cartas es {resultado}')
    return resultado

def run(NumeroCartas, Intentos):
    mazo = Barajas(Palos, Valores)
    manos = Simulacion(mazo, NumeroCartas, Intentos)
    # pares = Pares(manos)
    # trios = Trio(manos)
    escaleras = escalera(manos)
    probabilidad = Probabilidades(escaleras, Intentos, NumeroCartas)
    return probabilidad

if __name__ == '__main__':
    NumeroCartas = int(input('De cuantas Cartas desea que sea la mano: '))
    Intentos = int(input('cuantas veces quiere correr la simulacion: '))
    Probabilidad = run(NumeroCartas, Intentos)
    print(Probabilidad)