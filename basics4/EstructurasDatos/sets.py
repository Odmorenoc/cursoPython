
def Unicos(lista:list) -> list:
    return list(set(lista))

if __name__ == '__main__':
    lista = [1,1,2,2,4]
    unicos = Unicos(lista)
    print(f'de {lista} los valores unicos son: {unicos}')