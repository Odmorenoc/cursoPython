def divisors(num):
    divisor=[i for i in range(1,(num+1)) if num%i ==0]
    return divisor


def run():
    try:
        num=input(" por favor ingresa un numero: ")
        assert num.isnumeric() and int(num)>0, "valor ingresado invalido, por favor ingrese un número positivo"
        print(divisors(int(num)))
        print(num)
        print("Termino el programa")
    except AssertionError as ae:
        print(ae)
        run()

if __name__=="__main__":
    run()