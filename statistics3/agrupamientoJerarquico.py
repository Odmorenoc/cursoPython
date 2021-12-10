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

def Distancias(Vectores):
    
    distancias = {}
    a = 0
    for i in Vectores:
        b = 0
        for j in Vectores:
            clave = [a, b]
            clave = str(clave)
            if a != b:
                distancias[clave] = DistanciaEuclidiana(i, j)
            else:
                pass
            b += 1
        a += 1
    return distancias

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

def AgruparVectores(DistanciasVectores, Vectores):

    llave = min(DistanciasVectores, key=DistanciasVectores.get)
    valor = DistanciasVectores[llave]
    # print(f'La llave: {llave} \n tiene valor minimo: {valor}')
    
    vectores_agrupar = LeerClave(llave)
    a = int(vectores_agrupar[0])
    b = int(vectores_agrupar[1])
    vector1 = Vectores[a]
    vector2 = Vectores[b]

    vectorN = NuevoVector(vector1, vector2)

    if a > b:
        Vectores.pop(a)
        Vectores.pop(b)
    else: 
        Vectores.pop(b)
        Vectores.pop(a)
    
    Vectores.append(vectorN)

    return Vectores, vector1, vector2

def run(ListaVectores):
    if len(ListaVectores) > 1:
        distancias_vectores = Distancias(ListaVectores)
        intermedios = AgruparVectores(distancias_vectores, ListaVectores)
        nuevosVectores = intermedios[0]
        a = intermedios[1]
        b = intermedios[2]
        print(f'Se agruparon el vector {a} y {b} = {nuevosVectores[-1]}\nQuedando los {nuevosVectores} ')
        run(nuevosVectores)
    else:
        print(ListaVectores)
        

    pass

if __name__ == '__main__':
    vectores = Vectores(10)
    print(f'De los vectores {vectores}')
    run(vectores)
    print('fin')


    

        
    
