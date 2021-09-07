def potencias (rep,cont):
    if cont > rep:
        print("fin!")
    else : 
        print("2^"+ str(cont) + "="+ str(2**cont))
        potencias(rep,cont+1)

rep=int(input("¿cuantas repeticiones quiere reealizar? "))
potencias(rep,0)