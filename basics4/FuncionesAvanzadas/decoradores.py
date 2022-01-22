def funcion_decoradora(funcion):
    def wrapper():
        print('este es el ultimo mensaje ...')
        funcion()
        print('este es el primer mensaje')
    return wrapper()

# def zumbido():
#     print('buzzz')

# zumbido = funcion_decoradora(zumbido)

@funcion_decoradora
def zumbido():
	print("Buzzzzzz")



if __name__=='__main__':
    zumbido()