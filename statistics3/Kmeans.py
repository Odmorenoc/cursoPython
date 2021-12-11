import math
import random

def NuevoVector(Vector1, Vector2):
    
    x1 = Vector1[0]
    x2 = Vector2[0]
    y1 = Vector1[1]
    y2 = Vector2[1]

    x = round(float((x1 + x2) / 2), 2)
    y = round(float((y1 + y2) / 2), 2)

    vectorN = [x, y]

    return vectorN

def DistanciaEuclidiana(vector1, vector2):
    
    return round(math.sqrt((vector1[0] - vector2[0])**2 + (vector1[1] - vector2[1])**2), 2)

def Vectores(numVectores):
    
    Lista = []
    for i in range(numVectores):
        i = [random.randint(0, 10), random.randint(0, 10)]
        Lista.append(i)
    
    return Lista

def LeerClave(clave):
    a =''
    b =''
    i = ''
    for c in clave:
        if c == '[' or c == ' ':
            pass
        elif c == ',':
            break
        else: 
            a += c

    for c in clave[::-1]:
        if c == ']' or c == ' ':
            pass
        elif c == ',':
            break
        else: 
            i += c
            b = i[::-1]

    return a, b

def DistanciaMinima(Puntos, Centroides):

    distanciasMinimas = {}
    a = 0
    for centroide in Centroides:
        b = 0
        distancias = {}
        for punto in Puntos:
            clave = [a, b]
            clave = str(clave)
            distancias[clave] = DistanciaEuclidiana(centroide, punto)
            b += 1
        
        llave = min(distancias, key=distancias.get)
        valor = distancias[llave]
        distanciasMinimas[llave] = valor
        a += 1
    
    minimoCentroidePunto = min(distanciasMinimas, key=distanciasMinimas.get)
    Eliminar = LeerClave(minimoCentroidePunto)
    puntoEliminar = int(Eliminar[1])

    return puntoEliminar, minimoCentroidePunto

def Minimas(Puntos, Centroides):
    if len(Puntos) != 0:
        minima = DistanciaMinima(Puntos, Centroides)
        PuntoEliminar = minima[0]
        Clave = minima[1]
        diccionario= {}
        diccionario[Clave] = puntos[PuntoEliminar]
        puntos.pop(PuntoEliminar)
        nuevosPuntos = puntos
        distMinimas.append(diccionario)
        Minimas(nuevosPuntos, Centroides)

def NuevosCentroides(distancias_Minimas):
    centroide1x = 0.0
    centroide1y = 0.0
    centroide2x = 0.0
    centroide2y = 0.0
    centroide3x = 0.0
    centroide3y = 0.0
    centroide0x = 0.0
    centroide0y = 0.0
    a = 0
    b = 0
    c = 0
    d = 0

    for lista in distancias_Minimas:
        for llave, valor in lista.items():
            clave = LeerClave(llave)
            centroide = int(clave[0])
            if centroide == 0:
                centroide0x += valor[0]
                centroide0y += valor[1]
                a += 1
            elif centroide == 1:
                centroide1x += valor[0]
                centroide1y += valor[1]
                b += 1
            elif centroide == 2:
                centroide2x += valor[0]
                centroide2y += valor[1]
                c += 1
            elif centroide == 3:
                centroide3x += valor[0]
                centroide3y += valor[1]
                d += 1

    if a == 0:
        a = 1
    elif b == 0:
        b = 1
    elif c == 0:
        c = 1
    else:
        d = 1

    c0 = [round((centroide0x/a),2),round((centroide0y/a),2)]
    c1 = [round((centroide1x/b),2),round((centroide1y/b),2)]
    c2 = [round((centroide2x/c),2),round((centroide2y/c),2)]
    c3 = [round((centroide3x/d),2),round((centroide3y/d),2)]
    centroides = [c0, c1, c2, c3] 

    return centroides

if __name__ == '__main__':
    centroides = [[2.5, 2.5], [7.5, 2.5], [2.5, 7.5], [7.5, 7.5]]
    puntos = Vectores(10)
    tuplaPuntos = (puntos[:])
    print(tuplaPuntos)
    e = 1
    while e > 0.1:
        print(f'los centroides son:{centroides}\n')
        puntos = (tuplaPuntos[:])
        distMinimas = []
        Minimas(puntos, centroides)
        print(distMinimas)
        nuevos_centroides = NuevosCentroides(distMinimas)
        suma = 0.0
        a = 0
        for c in nuevos_centroides:
            b =0
            for c2 in centroides:
                if a == b:
                    distancia = DistanciaEuclidiana(c,c2)
                    suma += distancia
                    b += 1
                else:
                    b += 1
                    continue
            a += 1
        e = suma/4
        centroides = nuevos_centroides
    print(centroides)

