"""
6) Implemente uma classe chamada “Produto” que possua atributos para armazenar o
nome, o preço e a quantidade em estoque. Adicione métodos para calcular o valor
total em estoque e verificar se o produto está disponível.

"""

class Produto():
    def __init__(self, nome:str, preco:float, quantidade:int):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valorTotalEmEstoque(self):
        valorTotal = self.preco * self.quantidade
        print(f"O valor total em estoque é {valorTotal}")

    def disponibilidade(self):
        solicidado = int(input("Quantos produtos precisaria? "))
        if solicidado <= self.quantidade:
            restante = self.quantidade - solicidado
            print(f"Produto disponivel no estoque\nAinda restará {restante} em estoque")
        else:
            print(f"Não a quantidade o suficiente \nA quantidade disponivel desse produto é {self.quantidade}")
    

produto1 = Produto("Chocolate", 5.0, 1000)
produto1.valorTotalEmEstoque()
produto1.disponibilidade()