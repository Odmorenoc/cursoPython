import random
from typing import Coroutine
from bokeh.plotting import figure, show

class borrachos:
    
    def __init__(self, nombre):
        self.nombre = nombre

class borrachoTradicional(borrachos):
    
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

class borrachoLoco(borrachos):

    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):
        return random.choice([(random.randint(-1,1),random.randint(-1,1))])
        
class borrachoDiagonal(borrachos):
    
    def __init__(self,nombre):
        super().__init__(nombre)
    
    def camina(self):
        return random.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])


# class Coordenada =
class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def  mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y

        return (delta_x**2 + delta_y**2)**0.5

#class campo =
class Campo:
    def __init__(self) -> None:
        self.ubicacion_Borrachos = {}

    def anadir_borracho(self, borracho, coordenada):
        self.ubicacion_Borrachos[borracho] = coordenada

    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.ubicacion_Borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.ubicacion_Borrachos[borracho] = nueva_coordenada

    def obtener_coordenada(self, borracho):
        return self.ubicacion_Borrachos[borracho]

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))

    return distancias

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='distancia media')

    show(grafica)

def run(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []

    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

def main(distancia, inicio, borracho):
    campo = Campo()
    campo.anadir_borracho(borracho, inicio) #poner un borracho en origen
    ejecutar_caminata(campo, borracho, distancia)

def ejecutar_caminata(campo, borracho, distancia):
    x_arreglo = []
    y_arreglo = []
    x_arreglo.append(campo.obtener_coordenada(borracho).x)
    y_arreglo.append(campo.obtener_coordenada(borracho).y)
    for _ in range(distancia):
        campo.mover_borracho(borracho) #se actualiza las coordenadas del borracho
        x_arreglo.append(campo.obtener_coordenada(borracho).x)
        y_arreglo.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arreglo, y_arreglo)

def graficar(x, y):
    figura = figure()
    figura.line(x, y)
    show(figura)


if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    distancia = 1000

    inicio = Coordenada(0,0)
    borracho = borrachoLoco('Angel')
    main(distancia, inicio, borracho)

    #run(distancias_de_caminata, numero_de_intentos, borrachoTradicional)