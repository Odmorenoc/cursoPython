from random import randint
import os
import time



def adivinanza():
    palabra="loro"
    adivinador=""
    vidas=5
    while vidas > 0:
        fallas=0
        for i in palabra:
            if i in adivinador:
                print(i,end="")
            else:
                print("_ ",end="")
                fallas+=1
        if fallas==0:
            print("\nGanaste!")
            break

        l=input("\ningrese una letra\n")
        adivinador+=l.lower()

        if l not in palabra:
            vidas-=1
            print("te equivocaste, te quedan "+str(vidas)+" vidas")
            time.sleep(1)
        if vidas ==0:
            print("perdiste")
        os.system("clear")

adivinanza()

#sdlkfjdslkfjsn