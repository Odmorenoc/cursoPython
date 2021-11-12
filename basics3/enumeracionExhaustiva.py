# Enumeracion exhaustiva
# algoritmo para enumerar todas las posibilidades para adivinar  la raiz cuadrada exacta de un numero dado.

def run():
    objetivo = int(input("por favor ingrese un numero: "))
    i = 1
    while i**2 < objetivo:
        i+=1
        print(f'i es: {i}')

    if i**2 == objetivo:
        print(f'la raiz cuadrada exacta de {objetivo} es {i}')
    else:
        mayor = abs(objetivo - (i**2))
        menor = abs(objetivo - ((i-1)**2))
        if mayor > menor:
            i-=1
        print(f'la diferencia con i mayor es de {mayor} y con i menor es {menor}')
        print(f'la raiz cuadrada exacta más proxima a {objetivo} es {i}, es decir {i**2}')


if __name__=='__main__':
    run()