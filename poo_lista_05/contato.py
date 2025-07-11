from datetime import datetime

class Contato:
    def __init__(self, id, nome, email, fone, nascimento):
        self.id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nascimento(nascimento)

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_fone(self):
        return self.fone

    def set_fone(self, fone):
        self.fone = fone

    def get_nascimento(self):
        return self.nascimento

    def set_nascimento(self, nascimento):
        self.nascimento = nascimento

    def __str__(self):
        return f"ID: {self.id}\nnome: {self.nome}\nemail: {self.email}\nfone: {self.fone}\nnascimento: {self.nascimento}"

class ContatoUI:
    contatos = []
    id_atual = 0

    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()

            if interacao == 7:
                break

    @classmethod
    def menu(cls):
        print("1 - Inserir contato\n2 - Listar contatos\n3 - Excluir contatos\n4 - Atualizar contatos\n5 - Pesquisar contato\n6 - Aniversariantes\n7 - Sair")
        interacao = int(input())

        if interacao == 1:
            cls.inserir()
        elif interacao == 2:
            cls.listar()
        elif interacao == 3:
            cls.excluir()
        elif interacao == 4:
            cls.atualizar()
        elif interacao == 5:
            cls.pesquisar()
        elif interacao == 6:
            cls.aniversariantes()
        
        return interacao

    @classmethod
    def inserir(cls):
        nome = input("informe o nome: ")
        email = input("informe o email: ")
        fone = input("informe o fone: ")
        ano = int(input("informe o ano de nascimento: "))
        mes = int(input("informe o mês de nascimento: "))
        dia = int(input("informe o dia de nascimento: "))
        
        contato = Contato(cls.id_atual, nome, email, fone, datetime(ano, mes, dia))
        cls.id_atual += 1

        cls.contatos.append(contato)

    @classmethod
    def listar(cls):
        print("Contatos: ")
        for contato in cls.contatos:
            print(contato)

    @classmethod
    def excluir(cls):
        valor_id = input("Informe o ID do contato: ")
        for contato in cls.contatos:
            if contato.get_id() == valor_id:
                cls.contatos.remove(contato)

    @classmethod
    def atualizar(cls):
        cls.excluir()
        cls.inserir()

    @classmethod
    def pesquisar(cls):
        iniciais_informadas = input("Informe as iniciais do nome (ex.: g. i. d. s.): ")
        for contato in cls.contatos:
            nome = contato.nome
            iniciais = list(map(lambda x: x[0], nome.split(" ")))

            texto = ""
            for inicial in iniciais:
                texto = texto + inicial + ". "
            texto = texto[:-1]
            
            if texto == iniciais_informadas:
                print(contato)

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês: "))
        for contato in cls.contatos:
            if contato.get_nascimento().month == mes:
                print(f"contato: {contato.nome}, dia: {contato.get_nascimento().day}")

ContatoUI.main()