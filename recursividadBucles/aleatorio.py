import random


def run():
    r=random.randint(1,100)
    u=int(input("por favor escoja un numero entre el 1 y el 100: "))
    while u!=r:
        if u<r:
            u=int(input("intenta un numero más grande: "))
        else:
            u=int(input("intenta un numero más pequeño: "))
    print("Ganaste!!")

if __name__=="__main__":
    run()