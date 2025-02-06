"""
5) Crie uma classe chamada “Funcionário” com atributos para armazenar o nome, o 
salário e o cargo do funcionário. Implemente métodos para calcular o salário líquido, 
considerando descontos de impostos e benefícios.

"""

class Funcionario:
    def __init__(self, nome: str, salario: float, cargo:str):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcularSalarioLiquido(self):
        descontos = 200
        salarioBruto = self.salario - descontos
        print (f"O salário bruto do(a) {self.nome} é de {salarioBruto}")


funcionario1 = Funcionario("gabs", 10000, "Gerente")
funcionario1.calcularSalarioLiquido()
