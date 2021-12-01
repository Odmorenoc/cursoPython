import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    tiros_sin_1 = 0
    i = 0
    for tiro in tiros:
        i +=1
        if 1 not in tiro:
            tiros_sin_1 += 1
            print(f'en el tiro {i} no hay 1')
        else:
            tiros_con_1 += 1
            print(f'en el tiro {i} hay 1')

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    probabilidad_tiros_sin_1 = tiros_sin_1 / numero_de_intentos
    print(f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_sin_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)