"""
13) Implemente uma classe chamada “Agenda” que represente uma agenda telefônica.
Essa classe deve permitir adicionar, editar e remover contatos, além de buscar por
contatos a partir de um nome ou número de telefone.

"""

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionarContatos(self, contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} Adicionado com sucesso")


    def editarContato(self, nomeDoContato):
        for contato in self.contatos:
            if contato.nome == nomeDoContato:
                novoNome= input("Digite o novo nome: ")
                contato.nome = novoNome
                print(f"Nome alterado. Novo nome: {contato.nome}")
            else:
                print("Contato não encontrado")


    def removerContato(self, nomeDoContato):
        for contato in self.contatos:
            if contato.nome == nomeDoContato:
                self.contatos.remove(contato)
                print("Contato Removido")
            else:
                print("Contato não encontrado")

    def buscarPorNome(self, nomeDoContato):
        for contato in self.contatos:
            if contato.nome == nomeDoContato:
                print("Contato Encontrado")
                print(f"Nome: {contato.nome} e telefone {contato.telefone}")
            else:
                print("Contato não encontrado")

    def buscarPorTelefone(self, numeroTelefone):
        for contato in self.contatos:
            if contato.telefone == numeroTelefone:
                print("Contato Encontrado")
                print(f"Nome: {contato.nome} e telefone {contato.telefone}")
            else:
                print("Contato não encontrado")





#Objetos
contato1 = Contato("Gabs", 19987297781)
agenda = Agenda()

agenda.adicionarContatos(contato1)
# agenda.editarContato("Gabs")


# agenda.removerContato("Gabs")
# agenda.buscarPorNome("Gabs")
agenda.buscarPorTelefone(19987297781)

