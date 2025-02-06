"""
2) Implemente uma classe chamada “ContaBancária” que possua atributos para 
armazenar o número da conta, nome do titular e saldo. Adicione métodos para realizar 
depósitos e saques.

"""

class ContaBancaria:
    def __init__(self, titular:str, numero:int, saldo:float):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def depositar(self):
        deposito = float(input("Qual valor deseja depositar? "))
        self.saldo += deposito
        print(f"Seu saldo agora é {self.saldo}")

    def sacar(self):
        saque = float(input("Qual valor deseja sacar? "))
        self.saldo -= saque
        print(f"Seu saldo agora é {self.saldo}")


conta1 = ContaBancaria("Gabs", 1234567, 1000)

conta1.depositar()

conta1.sacar()