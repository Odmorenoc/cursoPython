# Se crea una comprensión de un diccionario cuyas llaves sean los primeros 100 N, y los valores sean los respectivos cubos desde 1 hasta el nuemro de la llave.
def run():
    dict= {}
    
    for i in range(1,101):
        dict[i]=[i**3 for i in range(1,i+1)]
    
    print(dict)


if __name__=="__main__":
    run()
