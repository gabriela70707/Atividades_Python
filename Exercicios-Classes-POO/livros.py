"""

10) Implemente uma classe chamada “Livro” com atributos para armazenar o título, o
autor e o número de páginas do livro. Adicione métodos para emprestar o livro,
devolvê-lo e verificar se está disponível.

"""

class Livro:
    def __init__(self, titulo:str, autor:str, numeroPaginas:int):
        self.titulo = titulo
        self.autor = autor
        self.numeroPaginas = numeroPaginas
        self.livro_emprestado = False

    def emprestarLivro(self):
        self.livro_emprestado = True

    def devolverLivro(self):
        self.livro_emprestado = False

    def verificarDisponibilidade(self):
        if self.livro_emprestado == False:
            print("O livro está disponivel")
        else:
            print("O livro está emprestado")


livro1 = Livro("Cronicas de Narnia", "CS. Lewis", 320)
livro1.emprestarLivro()
livro1.verificarDisponibilidade()