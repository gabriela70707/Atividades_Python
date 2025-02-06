"""
3) Crie uma classe chamada “Retângulo” que possua atributos para armazenar a largura e 
a altura. Implemente métodos para calcular a área e o perímetro do retângulo.


"""

class Retangulo:
    def __init__(self, largura:float, altura:float):
        self.altura = altura
        self.largura = largura

    def area(self):
        area = self.altura * self.largura
        print(area)

    def perimetro(self):
        perimetro = (2 * self.largura) + (2 * self.altura)
        print(perimetro)


forma1 = Retangulo(12, 10)

forma1.area()
forma1.perimetro()