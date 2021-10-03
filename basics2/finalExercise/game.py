import random
import os
import time

def letra(l):
    if l.isdigit():
        l=input("\ningrese una letra: \n")
        l=letra(l)
    else:
        l=l.lower()
    return l


def adivinanza(vidas, palabra, n):
    print(palabra)
    adivinador=""
    while vidas > 0:
        fallas=0
        for i in palabra[:n-1]:
            if i in adivinador:
                print(i,end="")
            else:
                print("_ ",end="")
                fallas+=1
        if fallas==0:
            print("\nGanaste!")
            break

        l=input("\ningrese una letra: \n")
        l=letra(l)
        adivinador+=l

        if l not in palabra[:n-1]:
            vidas-=1
            print("te equivocaste, te quedan "+str(vidas)+" vidas")
            time.sleep(1)
        if vidas ==0:
            print("perdiste")
        os.system("clear")


def run():
    animals=[]
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for animal in f:
            animals.append(animal)
    palabra=random.choice(animals)
    palabra=palabra.lower()
    n=len(palabra)
    # palabra="loro"
    print("Bienvenido al juego de hangman\n")
    vida=int(input(print("¿cuantos intentos quieres tener?")))
    adivinanza(vida,palabra, n)

    

if __name__=="__main__":
    run()