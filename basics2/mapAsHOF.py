def run():
    lista=[1,2,3,4,5]
    
    # #Se crea una nueva lista con los elmentos al cuadrado con un ciclo for:
    
    # square=[]

    # for i in lista:
    #     square.append(i**2)

    # #Se crea la misma lista con listComprehensions:

    # square=[i**2 for i in lista]

    # #Se crea la misma lista con la HOF map:

    square=list(map(lambda i: i**2, lista))

    print(square)


if __name__=="__main__":
    run()