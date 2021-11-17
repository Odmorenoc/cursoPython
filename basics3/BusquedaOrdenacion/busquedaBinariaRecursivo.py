import random
    
def busquedaBinaria(lista, objetivo, limInf, limSup):
    print(f'buscando {objetivo} entre {lista[limInf]} y {lista[limSup - 1]}')
    if limInf > limSup:
        return False 

    medio = (limInf + limSup) // 2

    if lista[medio] == objetivo:
        return True
    elif objetivo < lista[medio]:
        limSup = medio - 1
        return busquedaBinaria(lista, objetivo, limInf, limSup)
    elif objetivo > lista[medio]:
        limInf = medio + 1
        return busquedaBinaria(lista, objetivo, limInf, limSup)


if __name__ =='__main__':
    tamanoLista = int(input('tamaño de la lista: '))
    objetivo = int(input('objetivo: '))

    lista = sorted([random.randint(0, 100) for i in range(tamanoLista)])
    print(lista)
    respuesta = busquedaBinaria(lista, objetivo, 0, len(lista))
    print(f'el elemento {objetivo} {"esta" if respuesta else "no esta"} en la lista')