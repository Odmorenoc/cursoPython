class rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Cuadrado(rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)

class Triangulo(rectangulo):

    def __init__(self, base, altura):
        super().__init__(base, altura)

    def area(self):
        return super().area()/2
 

def run():
    Rectangulo = rectangulo(base = 3, altura = 4)
    print(Rectangulo.area())

    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())

    triangulo = Triangulo(4,3)
    print(triangulo.area())

if __name__ == '__main__':
    run()