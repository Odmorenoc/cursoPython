# Se crea una comprensión de un diccionario cuyas llaves sean los primeros 100 N, y los valores sean sus respectivos cubos.
def run():
    dict= {}
    nums=[i**3 for i in range(1,101)]
    for i in range(1,101):
        dict[i]=nums
    print(dict)

if __name__=="__main__":
    run()
