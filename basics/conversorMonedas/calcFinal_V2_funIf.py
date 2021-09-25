def moneda(bienvenida,pregunta):
    try:
        divisa=int(input(bienvenida + menu + pregunta))
    except:
         print("por favor escoja un valor numerico ")
         divisa=moneda(bienvenida,pregunta)
    return divisa


def valor():
    try:
        moneda=float(input("ingresa la cantidad que desea convertir: "))
    except:
        print("por favor escoja un valor numerico ")
        moneda=valor()
    return moneda


def divisa (opcion1):
    if opcion1==1:
        resultado="COP"
    elif opcion1==2:
        resultado="USD"
    else:
        resultado="MXN"
    return resultado


def run(opcion1,cantidad,opcion2):
    USD_COP= 3792.72
    USD_MXN= 19.92
    if opcion1==1:
        COP=cantidad
    elif opcion1==2:
        USD=cantidad
    else :
        MXN=cantidad
    if opcion1==1 and opcion2==2:
        resultado= (COP / USD_COP)
    elif opcion1==1 and opcion2==3:
        USD=(COP / USD_COP)
        resultado=USD*USD_MXN
    elif opcion1==2 and opcion2==1:
        resultado= (USD * USD_COP)
    elif opcion1==2 and opcion2==3:
        resultado= (USD * USD_MXN)
    elif opcion1==3 and opcion2==1:
        USD= (MXN / USD_MXN)
        resultado= (USD * USD_COP)
    elif opcion1==3 and opcion2==2:
        resultado= (MXN / USD_MXN)
    else: 
        print("Escogio la misma moneda")
        resultado=cantidad
    return resultado


if __name__=="__main__":
    inicio = str("Bienvenido al conversor de monedas, usted puede escoger entre estas opciones: ")
    menu="""
    1 - Pesos Colombianos (COP)
    2 - Dolares (USD)
    3 - Pesos Mexicanos (MXN)

    """
    moneda1 = str("por favor indique de que divisa quiere convertir: ")
    bienvenida = str("Escoja el tipo de moneda de destino")
    moneda2 = str("por favor indique a que divisa quiere convertir ")
    opcion1=moneda(inicio,moneda1)
    cantidad=valor()
    opcion2=moneda(bienvenida,moneda2)
    resultado=run(opcion1,cantidad,opcion2)
    print("se informa que $" + str(round(cantidad,0)) + " " + divisa(opcion1) + " son: $" + str(round(resultado,2)) + " " + divisa(opcion2))
