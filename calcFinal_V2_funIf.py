menu="""
1 - Pesos Colombianos (COP)
2 - Dolares (USD)
3 - Pesos Mexicanos (MXN)

"""
def conversor(opcion1,cantidad,opcion2):
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
def moneda1():
    try:
        divisa=int(input(menu + "por favor indique de que tipo de moneda quiere convertir: "))
    except:
         print("por favor escoja un valor numerico ")
         divisa=moneda1()
    return divisa
def valor():
    try:
        moneda=float(input("ingresa la cantidad que desea convertir: "))
    except:
        print("por favor escoja un valor numerico ")
        moneda=valor()
    return moneda
def moneda2 ():
    try:
        divisa2=int(input(print("Escoja el tipo de moneda de destino"+ menu + "por favor indique a que tipo de moneda quiere convertir ")))
    except:
         print("por favor escoja un valor numerico ")
         divisa2=moneda2()
    return divisa2
print("Bienvenido al conversor de monedas")
opcion1=moneda1()
cantidad=valor()
opcion2=moneda2()

resultado=conversor(opcion1,cantidad,opcion2)
print(str(round(resultado,2)))
#print("divisa inicial:"+str(opcion1))
#print("divisa final:"+str(opcion2))
#print("cantidad"+str(cantidad))