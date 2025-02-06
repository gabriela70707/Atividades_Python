"""
9) Crie uma classe chamada “Paciente” que possua atributos para armazenar o nome, a
idade e o histórico de consultas de um paciente. Implemente métodos para adicionar
uma nova consulta ao histórico e exibir as consultas realizadas.

"""

class Paciente:
    def __init__(self, nome, idade, historicoConsultas):
        self.nome = nome
        self.idade = idade
        self.historicoConsulta = historicoConsultas

    def adicionarConsulta(self):
        pass

    def exibirConsultas(self):
        pass