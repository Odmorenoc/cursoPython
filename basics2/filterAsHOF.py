def run():
    lista=[1,4,5,6,9,13,19,21]
    
    # #Se crea una depuración con un ciclo for:
    
    # depurada=[]

    # for i in lista:
    #     if i%2!=0:
    #         depurada.append(i)
    #     else:
    #         continue

    # #Se crea la misma depuración con listComprehensions:

    # depurada=[i for i in lista if i%2!=0]

    # #Se crea la misma depuración con la HOF filter:

    depurada=list(filter(lambda i: i%2!=0, lista))

    print(depurada)


if __name__=="__main__":
    run()