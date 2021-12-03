import random
import math
from bokeh.models.axes import Axis
from bokeh.plotting import figure, show

def media(X):
    return sum(X) / len(X)

def var(X):
    desviacion = 0
    desviaciones = []
    desviacionesCuadradas = []

    for i in X:
        desviacion = i - media(X)
        desviaciones.append(round(desviacion, 2))
        desviacionesCuadradas.append(desviacion**2)
    return sum(desviacionesCuadradas) / len(desviacionesCuadradas), desviaciones, desviacionesCuadradas

def gausiana(lista):
    miu = media(lista)
    intermedios = var(lista)
    sigma = intermedios[0]
    y = []
    
    for x in lista:
        y.append((1/(sigma*math.sqrt(2*math.pi)))*math.exp(-1/2*((x-miu)/(sigma))**2))
        
    
    grafica = figure(title=f'Distribución normal', x_axis_label='x', y_axis_label='y')
    
    grafica.line(lista, y, legend=f'Distribución normal',line_color='blue')

    show(grafica)
    

def run(lista):
    print(f'la lista de edades es: {lista}')
    print(f'la media de edades es: {media(lista)}')
    intermedios = var(lista)
    print(f'las variaciones de edad con respecto a la media son: {intermedios[1]}')
    print(f'la varianza de edades es: {round(intermedios[0], 2)}')
    print(f'la desviacion estandar es: {round((intermedios[0]**0.5), 2)}')
    gausiana(lista)


if __name__ == '__main__':

    edades = sorted([random.randint(1,40) for i in range(1000)])
    run(edades)
