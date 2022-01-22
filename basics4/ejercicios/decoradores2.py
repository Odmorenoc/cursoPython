def mayusculas(funcion):
    def envoltura(texto):
        return funcion(texto).upper()
    return envoltura

def mensajePersonalizado(mensaje):
    def conMensaje(funcion):
        print(f'{mensaje}')
        def envoltura(*args, **kwargs):
            resultado = funcion(*args, **kwargs)
            return resultado
        return envoltura 
    return conMensaje


# @mayusculas
@mensajePersonalizado(f'hola ')
def mensaje(nombre):
    return print(f'{nombre}, recibiste un mensaje') 

mensaje('oscar')