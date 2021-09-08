def run(rep,cont):
    if cont > rep:
        print("fin!")
    else : 
        print("2^"+ str(cont) + "="+ str(2**cont))
        potencias(rep,cont+1)

if __name__=="__main__":
    rep=int(input("¿cuantas repeticiones quiere reealizar? "))
    run(rep,0)