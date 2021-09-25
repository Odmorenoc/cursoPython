def run():
    n=int(input("escriba un numero para saber si es primo: "))
    r=0
    m=int(n**0.5)+1
    for i in range (2,m):
        if n%i==0:
            r=1
            break
        else:
            continue
        return r
    if r==0:
        print("es un numero primo!!")
    else:
        print("No es primo")


if __name__=="__main__":
    run()