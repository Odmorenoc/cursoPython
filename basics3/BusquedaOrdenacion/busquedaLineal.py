import random

def run (lista, objetivo):

    def busquedaLineal(lista, objetivo):
        match = False

        for i in lista:
            if i == objetivo:
                match = True
                break
        
        return match


if __name__ == '__main__':
    
    tamanoLista = int(input('tamaño de la lista: '))
    objetivo = int(input('objetivo: '))

    lista = [random.randint(0, 100) for i in range(tamanoLista)]
    print(lista)
    respuesta = run(lista, objetivo)
    print(f'el elemento {objetivo} {"esta" if respuesta else "no esta"} en la lista')
