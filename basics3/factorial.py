def run():
    factorial=int(input('por favor ingrese el factorial que desea obtener: '))
    
    def factorizacion(factorial):
        print(f'n = {factorial}')
        if factorial != 1:
            respuesta = factorial*factorizacion(factorial-1)
        else: 
            respuesta = 1
        return respuesta
        
    respuesta = factorizacion(factorial)

    print(f'el factorial de {factorial} es {respuesta}')


if __name__=='__main__':
    run()