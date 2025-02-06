"""
12) Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas
online. Essa classe deve ter funcionalidades para cadastrar produtos, gerar carrinho de
compras, aplicar descontos e calcular o valor total da compra.

"""

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class LojaVirtual:
    def __init__(self):
        self.produtos = []
        self.carrinho = []
    
    def cadastrarProduto(self, produto):
        self.produtos.append(produto)

    def gerarCarrinho(self, nomeDoProduto):
        for produto in self.produtos:
            if produto.nome == nomeDoProduto:
                self.carrinho.append(produto)
                print(f"Produto {produto.nome} Foi adicionado")
            else:
                print("Produto não encontrado")

    def aplicarDescontos(self, desconto, nomeDoProduto):
        for produto in self.carrinho:
            if produto.nome == nomeDoProduto:
                resultadoDescontado = (desconto/100) * produto.preco
                total = produto.preco - resultadoDescontado
                print(f"O produto {produto.nome} recebeu {desconto}% de desconto\nSeu valor ficou {total}")

    def totalDaCompra(self):
        total = sum(produto.preco for produto in self.carrinho) # somar todos os precos dos produtos que estão na lista self.carrinho
        print(f"O total é {total}")
        




#Objetos
produto1 = Produto("Chocolate", 12, 100)

loja = LojaVirtual() #instanciando a classe para poder usar suas funções

loja.cadastrarProduto(produto1) #cadastrando produtos

loja.gerarCarrinho("Chocolate") #Colocando no carrinho
# loja.totalDaCompra()


loja.aplicarDescontos(10,"Chocolate")
