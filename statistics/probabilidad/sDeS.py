from probabilidadesPoker import run

def PSimulacion(NumeroCartas, Intentos, Simulaciones):
    simulaciones = []
    for _ in range(Simulaciones):
        simulacion = run(NumeroCartas, Intentos)
        simulaciones.append(simulacion)
    
    return simulaciones

def PSimulaciones(simulaciones):  
    probabilidad = sum(simulaciones)/len(simulaciones)
    return probabilidad

if __name__ == '__main__':
    NumeroCartas = int(input(' De cuantas Cartas desea que sea la mano: '))
    Intentos = int(input('cuantas veces quiere correr la juego: '))
    SdS = int(input('cuantas veces quiere correr la simulacion: '))
    simulaciones = PSimulacion(NumeroCartas, Intentos, SdS)
    PdP = PSimulaciones(simulaciones)
    print(PdP)
    

