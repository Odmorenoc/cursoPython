import abc
import random

def tirar():
    tiro = random.choice([1, 2, 3, 4, 5, 6])
    return tiro

def jugada(cantDados):
    tiro = 0
    for _ in range(cantDados):
        tiro = tiro + tirar()
    return tiro

def dados(cantDados, numIntentos):
    secuenciaTiros = []
    tiro = 0
    for _ in range(numIntentos):
        tiro = jugada(cantDados)
        secuenciaTiros.append(tiro)
    return secuenciaTiros

def simulaciones(cantDados, numIntentos, numSimulaciones):
    simulacion = []
    for _ in range(numSimulaciones):
        secuenciaTiros = dados(cantDados, numIntentos)
        simulacion.append(secuenciaTiros)
    # print(simulacion)
    return simulacion
        
def probabilidades(simulacion, probabilidad):
    intentos = 0
    for i in simulacion:
        if probabilidad in i:
            intentos += 1
            # print(f'en la simualacion {i} hay por lo menos un {probabilidad}')
    
    return intentos

if __name__=='__main__':
    cantDados = int(input('Numero de dados que quieres tirar: '))
    numIntentos =  int(input('Numero de intentos que quieres tirar: '))
    numSimulaciones = int(input('Numero de simulaciones que quieres hacer: '))
    probabilidad = int(input('Hallar la probabilidad que salga el numero: '))
    simulacion = []
    simulacion = simulaciones(cantDados, numIntentos, numSimulaciones)
    # simulacion = simulaciones(2,10,1000) 
    # resultado = probabilidades(simulacion, 12) / 1000
    resultado = probabilidades(simulacion, probabilidad) / numSimulaciones
    print(f'la probabilidad de hallar un {probabilidad} en {numIntentos} intentos con {cantDados} dados es: {resultado}')
    # print(f'la probabilidad de hallar un 12 en 10 intentos con 2 dados es: {resultado}')
    