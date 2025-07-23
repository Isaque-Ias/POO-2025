import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.id = id
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

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


    def __str__(self):
        return f"CLiente\nID: {self.id}\nnome: {self.nome}\nemail: {self.email}\nfone: {self.fone}"

class ClienteUI:
    clientes = {}
    id_atual = 0

    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()

            if interacao == 8:
                break

    @classmethod
    def menu(cls):
        print("1 - Inserir cliente\n2 - Listar clientes\n3 - Mostrar cliente por ID\n4 - Atualizar cliente\n5 - Excluir cliente\n6 - Abrir lista de clientes\n7 - Salvar lista de clientes\n8 - Sair")
        interacao = int(input())

        if interacao == 1:
            cls.inserir()
        elif interacao == 2:
            cls.listar()
        elif interacao == 3:
            cls.listar_id()
        elif interacao == 4:
            cls.atualizar()
        elif interacao == 5:
            cls.excluir()
        elif interacao == 6:
            cls.abrir()
        elif interacao == 7:
            cls.salvar()
        
        return interacao

    @classmethod
    def inserir(cls):
        nome = input("informe o nome: ")
        email = input("informe o email: ")
        fone = input("informe o fone: ")
        
        cliente = Cliente(cls.id_atual, nome, email, fone)

        cls.clientes[str(cls.id_atual)] = cliente
        
        cls.id_atual += 1

    @classmethod
    def listar(cls):
        print("Contatos: ")
        for cliente in cls.clientes.items():
            print(cliente[1])

    @classmethod
    def listar_id(cls):
        valor_id = input("Informe o ID do contato: ")
        if cls.clientes.get(valor_id) == None:
            print("Contato não existe.")
            return
        print(cls.clientes[valor_id])

    @classmethod
    def excluir(cls):
        valor_id = input("Informe o ID do contato: ")
        if cls.clientes.get(valor_id) == None:
            print("Contato não existe.")
            return
        cls.clientes.pop(valor_id)

    @classmethod
    def atualizar(cls):
        cls.excluir()
        cls.inserir()

    @classmethod
    def abrir(cls):
        with open("poo_lista_06/cliente.json", "r") as file:
            json_dict = json.load(file)

        cls.clientes = {}
        for cliente in json_dict.items():
            cls.clientes[cliente[0]] = Cliente(cliente[1]["id"], cliente[1]["nome"], cliente[1]["email"], cliente[1]["fone"])

    @classmethod
    def salvar(cls):
        json_dict = {}
        for cliente in cls.clientes.items():
            json_dict[cliente[0]] = cliente[1].__dict__
            
        with open("poo_lista_06/cliente.json", "w") as file:
            json.dump(json_dict, file)

ClienteUI.main()