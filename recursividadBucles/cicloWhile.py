def run(limite):
    cont=0
    potencia_2=2**cont
    while potencia_2<=limite:
        print("2^" + str(cont) + " = " + str(potencia_2))
        cont= cont+1
        potencia_2 = 2**cont 
    pass

if __name__ =="__main__":
    limite=int(input("hasta que limite quiere encontar la potencia exacta?: "))
    run(limite)