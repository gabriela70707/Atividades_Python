"""
4) Implemente uma classe chamada “Aluno” que possua atributos para armazenar o 
nome, a matrícula e as notas de um aluno. Adicione métodos para calcular a média das 
notas e verificar a situação do aluno (aprovado ou reprovado).

"""

class Aluno:
    def __init__(self, nome:str, matricula:int):
        self.nome = nome
        self.matricula = matricula
        self.notas = []


    def media(self):
        #Adicionando as notas
        for i in range (0, 5):
            nota = int(input(f"Digite a {i + 1} nota do aluno: "))
            self.notas.append(nota)
    
        #Calculando a media
        total = sum(self.notas) #Soma os itens dentro da lista
        self.media = total / len(self.notas) #Divide os itens de dentro da lista pelo seu tamanho

        print(f"A media do aluno é: {self.media}")




    def verificarSituacao(self):
          #Verificando a situação do aluno
        if self.media >= 6 :
            print("O Aluno foi aprovado")
        else:
            print("Infelimente o aluno reprovou")
    



aluno1 = Aluno("Joyce", 1234567)
aluno1.media()

aluno1.verificarSituacao()