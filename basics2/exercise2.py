def run():
    # Se crea un diccionario cuyas llaves sean los primeros 100 N, y los valores sean los respectivos cubos desde 1 hasta el numero de la llave.

    #     dict= {}
    
    #     for i in range(1,101):
    #         dict[i]=[i**3 for i in range(1,i+1)]

    ## se crea el dictionary comprehension
    
    # dict={i:[i**3 for i in range(1,i+1)] for i in range(1,101)}

    # Se crea un diccionario cuyas llaves sean los numeros multiplos de 3 entre 1 y 100, y los valores sean los respectivos cubos desde 1 hasta el numero de la llave.

    #     dict= {}
    
    #     for i in range(1,101):
    #         if i%3 == 0 :
    #             dict[i]=[i**3 for i in range(1,i+1) if i%3 == 0]
    #         else:
    #             continue

    ## se crea el dictionary comprehension 

    # dict = {
    #     i : [i**3 for i in range(1,i+1) if i%3 == 0] for i in range(1,100) if i%3 == 0}
    
    print(dict)
    

if __name__=="__main__":
    run()
