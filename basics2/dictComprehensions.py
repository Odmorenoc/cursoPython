# Se crea una comprensión de un diccionario cuyas llaves sean los primeros 100 N, y los valores sean los respectivos cubos desde 1 hasta el numero de la llave.

# def run():
#     dict= {}
    
#     for i in range(1,101):
#         dict[i]=[i**3 for i in range(1,i+1)]
    
#     print(dict)

# Se crea una comprensión de un diccionario cuyas llaves sean los numeros multiplos de 3 entre 1 y 100, y los valores sean los respectivos cubos desde 1 hasta el numero de la llave.

def run():
    dict= {}
    keys=[i for i in range(1,101) if i%3 == 0]
    
    for i in range(1,101):
        if i%3 == 0 :
            a=i
            dict[a]=[i**3 for i in range(1,i+1) if i%3 == 0]
        else:
            continue
        
    
    print(dict)

if __name__=="__main__":
    run()
