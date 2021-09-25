def run(limite):
    for cont in range (limite+1):
        print("2^" + str(cont) + " = " + str(2**cont))

if __name__ =="__main__":
    limite=int(input("hasta que potencia quiere encontrar el resultado?: "))
    run(limite)