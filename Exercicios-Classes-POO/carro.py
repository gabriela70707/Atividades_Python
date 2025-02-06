"""
8) Implemente uma classe chamada “Carro” com atributos para armazenar a marca, o
modelo e a velocidade atual do carro. Adicione métodos para acelerar, frear e exibir a
velocidade atual.

"""

class Carro:
    def __init__(self, marca:str, modelo:str, velocidade_atual:int):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual

    def acelerar(self, acelerar):
        self.velocidade_atual += acelerar
        print(f"Sua velocidade no momento é {self.velocidade_atual}")
        

    def frear(self):
        while self.velocidade_atual > 0:
            self.velocidade_atual -= 1
            print(f"Sua velocidade é {self.velocidade_atual}")
          
        
        print(f"Você freou, sua velocidade atual é {self.velocidade_atual}")

    def exibirVelocidadeAtual(self):
        print(f"Sua velocidade atual é: {self.velocidade_atual}")


carro1 = Carro("Renault", "Kwid", 100)
carro1.acelerar(10)
carro1.frear()
carro1.exibirVelocidadeAtual()