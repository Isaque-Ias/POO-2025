import json
from datetime import datetime
import os

current_folder = os.path.dirname(os.path.abspath(__file__))

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
    contatos = {}
    id_atual = 0

    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()

            if interacao == 10:
                break

    @classmethod
    def menu(cls):
        print("1 - Inserir contato\n2 - Listar contatos\n3 - Listar contato por ID\n4 - Excluir contatos\n5 - Atualizar contatos\n6 - Pesquisar contato\n7 - Aniversariantes\n8 - Abrir contatos\n9 - Salvar contatos\n10 - Sair")
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
            cls.abrir()
        elif interacao == 9:
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
        
        contato = Contato(cls.id_atual, nome, email, fone, datetime(ano, mes, dia))
        
        cls.contatos[str(cls.id_atual)] = contato

        cls.id_atual += 1

    @classmethod
    def listar(cls):
        print("Contatos: ")
        for contato in cls.contatos.items():
            print(contato[1])

    @classmethod
    def listar_id(cls):
        valor_id = input("Informe o ID do contato: ")
        if cls.contatos.get(valor_id) == None:
            print("Contato não existe.")
            return
        print(cls.contatos[valor_id])

    @classmethod
    def excluir(cls):
        valor_id = input("Informe o ID do contato: ")
        if cls.contatos.get(valor_id) == None:
            print("Contato não existe.")
            return
        cls.clientes.pop(valor_id)

    @classmethod
    def atualizar(cls):
        cls.excluir()
        cls.inserir()

    @classmethod
    def pesquisar(cls):
        iniciais_informadas = input("Informe as iniciais do nome (ex.: g. i. d. s.): ")
        for contato in cls.contatos.items():
            nome = contato[1].nome
            iniciais = list(map(lambda x: x[0], nome.split(" ")))

            texto = ""
            for inicial in iniciais:
                texto = texto + inicial + ". "
            texto = texto[:-1]
            
            if texto == iniciais_informadas:
                print(contato[1])

    @classmethod
    def aniversariantes(cls):
        mes = int(input("Informe o mês: "))
        for contato in cls.contatos.items():
            if contato[1].get_nascimento().month == mes:
                print(f"contato: {contato[1].nome}, dia: {contato[1].get_nascimento().day}")

    @classmethod
    def abrir(cls):
        with open(current_folder + "\\contato.json", "r") as file:
            json_dict = json.load(file)

        cls.contato = {}
        for contato in json_dict.items():
            cls.contatos[contato[0]] = Contato(contato[1]["id"], contato[1]["nome"], contato[1]["email"], contato[1]["fone"], datetime(contato[1]["nascimento"][0], contato[1]["nascimento"][1], contato[1]["nascimento"][2]))

    @classmethod
    def salvar(cls):
        json_dict = {}
        for contato in cls.contatos.items():
            json_dict[contato[0]] = contato[1].__dict__
            json_dict[contato[0]]["nascimento"] = [contato[1].nascimento.year, contato[1].nascimento.month, contato[1].nascimento.day]
            
        with open(current_folder + "\\contato.json", "w") as file:
            json.dump(json_dict, file)

ContatoUI.main()