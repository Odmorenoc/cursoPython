# Aproximación de soluciones
# Algoritmo para enumerar todas las soluciones con un error menor a epsilon.
# Problema: hallar la raiz cuadrada más cercana al numero dado por el usuario.

menu ='''Este programa devuelve la raiz cuadrada más aproximada por dos metodos:
1. Enumeración exhaustiva
2. Busqueda binaria

''' 


def aproximacionExhaustiva():
    objetivo = int(input('por favor ingrese un número para encontrar su raiz cuadrada: '))
    respuesta = 0.0
    epsilon = 0.001
    i = epsilon**2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'respuesta es {respuesta}')
        respuesta += i

    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada exacta de {objetivo} es {respuesta}')
    else:
        mayor = abs(objetivo - (respuesta**2))
        menor = abs(objetivo - ((respuesta-i)**2))
        if mayor > menor:
            i-=1
        print(f'la diferencia con i mayor es de {mayor} y con i menor es {menor}')
        print(f'la raiz cuadrada más proxima a {objetivo} con un error menor a {epsilon}, es {respuesta}')

# para la utilización de busqueda binaria, se de cumplir con que el requisito que la respuesta buscada se encuentre dentro de un conjunto ordenado.
def busquedaBinaria():
    objetivo = int(input('por favor ingrese un número para encontrar su raiz cuadrada: '))
    epsilon = 0.001
    i = epsilon**2
    lim_inf = 0.0
    lim_sup = max(1.0, objetivo)
    respuesta = (lim_sup + lim_inf) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            lim_inf = respuesta
        else:
            lim_sup = respuesta
        print(f'respuesta es {respuesta}')
        respuesta = (lim_sup + lim_inf) / 2
    
    if respuesta**2 == objetivo:
        print(f'la raiz cuadrada exacta de {objetivo} es {respuesta}')
    else:
        mayor = abs(objetivo - (respuesta**2))
        menor = abs(objetivo - ((respuesta-epsilon)**2))
        if mayor > menor:
            i-=1
        print(f'la diferencia con i mayor es de {mayor} y con i menor es {menor}')
        print(f'la raiz cuadrada más proxima a {objetivo} con un error menor a {epsilon}, es {respuesta}')


if __name__=='__main__':
    metodo = int(input(f'{menu}Seleccione el metodo de calculo de la raiz cuadrada que desea utilizar: '))

    if metodo == 1:
        aproximacionExhaustiva()
    else:
        busquedaBinaria()
    