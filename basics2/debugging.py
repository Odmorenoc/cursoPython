def divisors(num):

    #Se aprende a la depuración de errores con run and debug de VScode.
    #Se crea un breakpoint en la linea 4 en la cual se intuye existe el error.
    #se corrige el error correspondiente al resultado del modulo de la condicion.

    divisor=[i for i in range(1,(num+1)) if num%i ==0]
    return divisor


def run():

    # se corrige el error si el usuario ingresa una letra.
    
    try:
        num=int(input(" por favor ingresa un numero: "))
        if num > 0:
            print(divisors(num))
            print(num)
            print("Termino el programa")
        else: 
            raise ValueError
    except ValueError:
        print("el valor ingresado no es permitido, ingrese solo numeros positivos")
        run()
    pass


if __name__=="__main__":
    run()