def run():
    lista=[1,2,3,4,5]
    
    #genera la multiplicación consecutivade los valores de una lista:
    
    # t=1
    
    # for i in lista:
    #     t*=i
    
    # #Se crea la misma lista con la HOF map:

    from functools import reduce

    result=reduce(lambda a,b: a*b, lista)

    print(result)
    # print(t)


if __name__=="__main__":
    run()