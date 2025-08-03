from view.view import View

class UI:
    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()

            if interacao == 9:
                break

    @classmethod
    def menu(cls):
        print("1 - Inserir contato\n2 - Listar contatos\n3 - Listar contato por ID\n4 - Excluir contatos\n5 - Atualizar contatos\n6 - Pesquisar contato\n7 - Aniversariantes\n8 - Salvar contatos\n9 - Sair")
        interacao = int(input())

        if interacao == 1:
            cls.inserir()
        elif interacao == 2:
            cls.listar()
        elif interacao == 3:
            cls.listar_id()
        elif interacao == 4:
            cls.excluir()
        elif interacao == 5:
            cls.atualizar()
        elif interacao == 6:
            cls.pesquisar()
        elif interacao == 7:
            cls.aniversariantes()
        elif interacao == 8:
            cls.salvar()
        
        return interacao
    
    @classmethod
    def inserir(cls):
        nome = input("informe o nome: ")
        email = input("informe o email: ")
        fone = input("informe o fone: ")
        ano = int(input("informe o ano de nascimento: "))
        mes = int(input("informe o mês de nascimento: "))
        dia = int(input("informe o dia de nascimento: "))

        View.inserir(nome, email, fone, ano, mes, dia)

    @classmethod
    def listar(cls):
        print("Clientes:")
        for contato in View.listar().items():
            print(contato)

    @classmethod
    def listar_id(cls):
        id = input("Informe o ID.")
        contato = View.listar_id(id)
        if contato:
            print(contato)
        else:
            print("Contato não existe.")

    @classmethod
    def excluir(cls):
        id = input("Informe o ID.")
        View.excluir(id)

    @classmethod
    def atualizar(cls):
        cls.excluir()
        cls.inserir()

    @classmethod
    def pesquisar(cls):
        iniciais_informadas = input("Informe as iniciais do nome (ex.: g. i. d. s.): ")
        print(View.pesquisar(iniciais_informadas))

    
    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês: "))
        for contato in View.aniversariantes(mes):
                print(f"contato: {contato.nome}, dia: {contato.get_nascimento().day}")

    @classmethod
    def salvar(cls):
        View.salvar()