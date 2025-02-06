"""
1) Crie uma classe chamada “Círculo” que possua um atributo para armazenar o raio e 
métodos para calcular a área e o perímetro do círculo.

"""
import math

class Circulo:
    

    def __init__(self, raio:int):
        self.raio = raio

    def calcular_Area(self):
        area = math.pi * math.pow(self.raio, 2)
        print(area)
    
    def calcularPerimetro(self):
        perimetro = 2 * math.pi * self.raio
        print(perimetro)
         

circulo1 = Circulo(120)

circulo1.calcular_Area()

circulo1.calcularPerimetro()