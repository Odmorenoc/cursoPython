def primalidad(n: int) -> bool:
    raiz: int =int(n**0.5)+1
    divisores : list[int] = [i for i in range(2, raiz) if n % i == 0]
    esPrimo : bool = len(divisores) == 0
    return esPrimo
        

if __name__=="__main__":
    n: int =int(input("escriba un numero para saber si es primo: "))
    primo: bool = primalidad(n)
    if primo == True:
        print("es un numero primo!!")
    else:
        print("No es primo")