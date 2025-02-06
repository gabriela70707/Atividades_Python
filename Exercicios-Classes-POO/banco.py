"""
11) Implemente uma classe chamada “Banco” que represente uma instituição financeira.
Essa classe deve conter métodos para cadastrar clientes, abrir contas bancárias e
realizar operações como saques, depósitos e transferências.

"""

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = [] 

    def cadastrarClientes(self, nomeTitular:str,idade:int, saldo:float, numeroConta:int):
        self.nomeTitular = nomeTitular
        self.idade = idade
        self.saldo = saldo
        self.numeroConta = numeroConta

    def abrirContas(self, conta):
        self.contas.append(conta) #preenchendo a lista contas
        print("Conta aberta com sucesso")
    
    def sacar(self):
        valor = int(input("Digite o valor que deseja sacar: "))
        self.saldo -= valor
        print(f"Seu saldo é {self.saldo}")


    def depositar(self):
        valor = int(input("Digite o valor que deseja depositar: "))
        self.saldo += valor
        print(f"Seu saldo é {self.saldo}")


    def transferir(self):
        valor = int(input("Digite o valor que deseja trasferir: "))
        self.saldo -= valor
        print(f"Seu saldo é {self.saldo}")



#Objetos
conta1 = Banco("Gabs")
conta1.cadastrarClientes("Gabriela", 19, 1000, 1234567)
conta1.abrirContas(conta1)
conta1.transferir()