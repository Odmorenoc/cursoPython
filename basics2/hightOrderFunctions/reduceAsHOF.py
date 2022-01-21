def run():
    lista=[1,2,3,4,5]
    
    #Se crea una nueva lista con los elementos al cuadrado con un ciclo for:
    
    # result=[]
    # t=1
    
    # for i in lista:
    #     t*=i
    #     result.append(t)

    # #Se crea la misma lista con listComprehensions:

    

    # #Se crea la misma lista con la HOF map:

    from functools import reduce

    result=reduce(lambda a,b: a*b, lista)

    print(result)


if __name__=="__main__":
    run()