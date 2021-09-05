USD_COP= 3792.72
USD_MXN= 19.92
menu="""

1 - Pesos Colombianos (COP)
2 - Dolares (USD)
3 - Pesos Mexicanos (MXN)

"""
print("Bienvenido al conversor de monedas")
opcion1=int(input(menu + "por favor indique de que tipo de moneda quiere convertir "))
if opcion1==1:
    COP = float(input("ingresa la cantidad de COP que desea convertir: "))
    USD =str(round((COP / USD_COP),2))
    opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir ")))
    if opcion2==opcion1: 
        opcion2=int(input(print("por favor indique de a qur tipo de moneda quiere convertir, diferente a COP ")))
        if opcion2==2:
            print("Tienes $" + USD + " USD")
        else:
            USD=COP/USD_COP
            MXN=str(USD*USD_MXN)
            print("Tienes $" + MXN + " MXN")
    else:
        if opcion2==2:
            print("Tienes $" + USD + " USD")
        else:
            USD=COP/USD_COP
            MXN=str(round((USD*USD_MXN),2))
            print("Tienes $" + MXN + " MXN")
elif opcion1==2:
    USD = float(input("ingresa la cantidad de USD que desea convertir: "))    
    opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir: ")))
    if opcion2==opcion1:
        opcion2=int(input(print("por favor indique de a que tipo de moneda quiere convertir, diferente a USD: ")))
        if opcion2==1:
            COP=str(round((USD*USD_COP),2))
            print("Tienes $" + COP + " COP")
        else:
            MXN=str(round((USD*USD_MXN),2))
            print("Tienes $" + MXN + " MXN")
    else:
        if opcion2==1:
            COP=str(USD*USD_COP)
            print("Tienes $" + COP + " COP")
        else:
            MXN=str(USD*USD_MXN)
            print("Tienes $" + MXN + " MXN")
elif opcion1==3:
    MXN = float(input("ingresa la cantidad de MXN que desea convertir: "))    
    opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir: ")))    
    USD=round((MXN/USD_MXN),2) 
    if opcion2==opcion1:
        opcion2=int(input(print("por favor indique de a que tipo de moneda quiere convertir diferente a MXN: ")))
        if opcion2==1:
            COP=str(round((USD*USD_COP),2))
            print("Tienes $" + COP + " COP")
        else:
           print("Tienes $" + str(USD) + " USD")
    else:
        if opcion2==1:
            COP=str(round((USD*USD_COP),2))
            print("Tienes $" + COP + " COP")
        else:
           print("Tienes $" + str(USD) + " USD")
else:
    opcion1=int(input("por favor escoja una opción valida: "))
    if opcion1==1:
        COP = float(input("ingresa la cantidad de COP que desea convertir: "))
        USD =str(round((COP / USD_COP),2))
        opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir ")))
        if opcion2==opcion1: 
            opcion2=int(input(print("por favor indique a que tipo de moneda quiere convertir, diferente a COP: ")))
            if opcion2==2:
                print("Tienes $" + USD + " USD")
            else:
                USD=COP/USD_COP
                MXN=str(USD*USD_MXN)
                print("Tienes $" + MXN + " MXN")
        else:
            if opcion2==2:
                print("Tienes $" + USD + " USD")
            else:
                USD=COP/USD_COP
                MXN=str(round((USD*USD_MXN),2))
                print("Tienes $" + MXN + " MXN")
    elif opcion1==2:
        USD = float(input("ingresa la cantidad de USD que desea convertir: "))    
        opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir: ")))
        if opcion2==opcion1:
            opcion2=int(input(print("por favor indique de a que tipo de moneda quiere convertir, diferente a USD: ")))
            if opcion2==1:
                COP=str(round((USD*USD_COP),2))
                print("Tienes $" + COP + " COP")
            else:
                MXN=str(round((USD*USD_MXN),2))
                print("Tienes $" + MXN + " MXN")
        else:
            if opcion2==1:
                COP=str(USD*USD_COP)
                print("Tienes $" + COP + " COP")
            else:
                MXN=str(USD*USD_MXN)
                print("Tienes $" + MXN + " MXN")
    elif opcion1==3:
        MXN = float(input("ingresa la cantidad de MXN que desea convertir: "))    
        opcion2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique de a que tipo de moneda quiere convertir: ")))    
        USD=round((MXN/USD_MXN),2) 
        if opcion2==opcion1:
            opcion2=int(input(print("por favor indique a que tipo de moneda quiere convertir, diferente a MXN: ")))
            if opcion2==1:
                COP=str(round((USD*USD_COP),2))
                print("Tienes $" + COP + " COP")
            else:
                print("Tienes $" + str(USD) + " USD")
        else:
            if opcion2==1:
                COP=str(round((USD*USD_COP),2))
                print("Tienes $" + COP + " COP")
            else:
                print("Tienes $" + str(USD) + " USD")