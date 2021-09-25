USD_COP= 3792.72
USD_MXN= 19.92
menu="""

1 - Pesos Colombianos (COP)
2 - Dolares (USD)
3 - Pesos Mexicanos (MXN)

"""


def moneda1():
    divisa=input(menu + "por favor indique de que tipo de moneda quiere convertir ")
    return divisa


def cantidad():
    moneda=float(input("ingresa la cantidad que desea convertir: "))
    return moneda


def moneda2 ():
    divisa2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir ")))
    return divisa2


def cambio():
    opcion2=int(input(print("por favor indique un tipo de moneda diferente: ")))
    return opcion2


def a_dolar(COP,MXN,USD_COP,USD_MXN):
    if COP != 0:
        USD = (COP / USD_COP)
    else:
        USD = (MXN / USD_MXN)
    return USD


def a_pesos(opcion2,USD,USD_COP,USD_MXN):
    if opcion2==1:
        pesos=USD*USD_COP
    else: 
        pesos=USD*USD_MXN
    return pesos


def error1(opcion1):
    if opcion1==("1" or "2" or "3"):
            conversor(int(opcion1))
    else:
        opcion1=input("por favor escoja una opción entre 1, 2 o 3 unicamente: ")
        error1(opcion1)


def run(opcion1):
    if int(opcion1)==1:
        COP=cantidad()
        MXN=0
        opcion2=moneda2()
        if opcion2==opcion1 :
            opcion2=cambio()
            if opcion2==2:
                print("Tienes $" + str(round(a_dolar(COP,MXN,USD_COP,USD_MXN),2)) + " USD")
            else:
                USD=a_dolar(COP,MXN,USD_COP,USD_MXN)
                print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " MXN")
        elif opcion2==2:
            print("Tienes $" + str(round(a_dolar(COP,MXN,USD_COP,USD_MXN),2)) + " USD")
        else:
            USD=a_dolar(COP,MXN,USD_COP,USD_MXN)
            print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " MXN")
    elif int(opcion1)==2:
        USD=cantidad()
        opcion2=moneda2()
        if opcion2==opcion1 :
            opcion2=cambio()
            if opcion2==1:
                print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " cop")
            else:
                print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " MXN")
        elif opcion2==1:
            print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " cop")
        else:
            print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " MXN")
    elif int(opcion1)==3:
        MXN=cantidad()
        COP=0
        opcion2=moneda2()
        if opcion2==opcion1 :
            opcion2=cambio()
            if opcion2==1:
                USD=a_dolar(COP,MXN,USD_COP,USD_MXN)
                print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " COP")
            else:
                print("Tienes $" + str(round(a_dolar(COP,MXN,USD_COP,USD_MXN),2)) + " USD")
        elif opcion2==1:
            USD=a_dolar(COP,MXN,USD_COP,USD_MXN)
            print("Tienes $" + str(round(a_pesos(opcion2,USD,USD_COP,USD_MXN),2)) + " COP")
        else:
            print("Tienes $" + str(round(a_dolar(COP,MXN,USD_COP,USD_MXN),2)) + " USD")
    else:
        opcion1=input("por favor escoja una opción valida: ")
        error1(opcion1)


if __name__=="__main__":
    print("Bienvenido al conversor de monedas")
    opcion1=moneda1()
    run(int(opcion1))