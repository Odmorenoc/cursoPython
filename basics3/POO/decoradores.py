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


# class votacion:

#     def __init__(self, id, pais):
#         self.id = id
#         self.__pais = pais
#         self.__region = None

#     @property
#     def region(self):
#         return self.__region

#     @region.setter
#     def region(self, region):
#         if region in self.__pais:
#             self.__region = region
#         else:
#             raise ValueError(f'La region {region} no es valida en {self.__pais}')

# casilla = votacion(1, ['CDMX', 'Morelos'])
# print(casilla.region)
# casilla.region = 'CDMX'
# print(casilla.region)
# casilla.region = 'Bogota'
# print(casilla.region)


if __name__=='__main__':
    zumbido()