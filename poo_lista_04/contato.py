class Contato:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.nome = nome
        self.__email = email
        self.__fone = fone

    def get_id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.__id}\nnome: {self.nome}\nemail: {self.__email}\nfone: {self.__fone}"

class ContatoUI:
    contatos = []

    @staticmethod
    def main():
        while True:
            interacao = ContatoUI.menu()

            if interacao == 6:
                break

    def menu():
        print("1 - Inserir contato\n2 - Listar contatos\n3 - Excluir contatos\n4 - Atualizar contatos\n5 - Pesquisar contato\n6 - Sair")
        interacao = int(input())

        if interacao == 1:
            ContatoUI.inserir()
        elif interacao == 2:
            ContatoUI.listar()
        elif interacao == 3:
            ContatoUI.excluir()
        elif interacao == 4:
            ContatoUI.atualizar()
        elif interacao == 5:
            ContatoUI.pesquisar()
        
        return interacao

    @staticmethod
    def inserir():
        id = input("informe o ID: ")
        nome = input("informe o nome: ")
        email = input("informe o email: ")
        fone = input("informe o fone: ")
        
        contato = Contato(id, nome, email, fone)

        ContatoUI.contatos.append(contato)

    @staticmethod
    def listar():
        print("Contatos: ")
        for contato in ContatoUI.contatos:
            print(contato)

    @staticmethod
    def excluir():
        valor_id = input("Informe o ID do contato: ")
        for contato in ContatoUI.contatos:
            if contato.get_id() == valor_id:
                ContatoUI.contatos.remove(contato)

    @staticmethod
    def atualizar():
        ContatoUI.excluir()
        ContatoUI.inserir()

    @staticmethod
    def pesquisar():
        iniciais_informadas = input("Informe as iniciais do nome (ex.: g. i. d. s.): ")
        for contato in ContatoUI.contatos:
            nome = contato.nome
            iniciais = list(map(lambda x: x[0], nome.split(" ")))

            texto = ""
            for inicial in iniciais:
                texto = texto + inicial + ". "
            texto = texto[:-1]
            
            if texto == iniciais_informadas:
                print(contato)

ContatoUI.main()