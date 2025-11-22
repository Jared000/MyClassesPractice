import math 

class Figura:
    def area(self):
        pass
    def perimetro(self):
        pass

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado = lado 

    def area(self):
        return self.lado * self.lado
    
    def perimetro(self):
        return self.lado *4
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi* self.radio*self.radio
    def perimetro(self):
        return math.pi* self.radio *2
    
lista = [Cuadrado(2) ,Circulo(2)]

for Figura in lista:
    print(Figura.area(), Figura.perimetro())