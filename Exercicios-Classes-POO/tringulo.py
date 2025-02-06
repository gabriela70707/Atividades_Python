"""
7) Crie uma classe chamada “Triângulo” com atributos para armazenar os três lados do
triângulo. Implemente métodos para verificar se é um triângulo válido e calcular sua
área.

"""

class Triangulo:
    def __init__(self, altura1:int, altura2:int, base:int):
        self.altura1 = altura1
        self.altura2 = altura2
        self.base = base

    def verificar(self):
        desigualdade = self.altura1 + self.altura2
        if desigualdade > self.base:
            print("Esse é um triângulo válido")
        else:
            print("Isso não é um triângulo")

    def calcularArea(self):
        area = (self.altura1 * self.base)/2
        print(area)


#objetos
triangulo1 = Triangulo(5, 5, 7)
triangulo1.verificar()
triangulo1.calcularArea()