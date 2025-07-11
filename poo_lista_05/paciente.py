from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        if not cpf.isdigit():
            raise ValueError()

        self.cpf = cpf

    def get_telefone(self):
        return self.telefone
    
    def set_telefone(self, telefone):
        if not telefone.isdigit():
            raise ValueError()

        self.telefone = telefone

    def get_nascimento(self):
        return self.nascimento

    def set_nascimento(self, nascimento):
        self.nascimento = nascimento

    def idade(self):
        d1 = self.nascimento
        d2 = datetime.now()

        year_difference = d2.year - d1.year
        month_difference = d2.month - d1.month

        if d2.day < d1.day:
            month_difference -= 1

        if month_difference < 0:
            year_difference -= 1
            month_difference += 12

        return f"anos: {year_difference}, meses: {month_difference}"

    def __str__(self):
        return f"nome: {self.get_nome()}, cpf: {self.get_cpf()}, telefone: {self.get_telefone()}, nascimento: {self.get_nascimento()}"

class PacienteUI:
    pacientes = []

    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()
            if interacao == 5:
                break

    @classmethod
    def menu(cls):
        print("1 - cadastrar paciente\n2 - ver pacientes\n3 - deletar paciente\n4 - alterar paciente\n5 - sair")
        interacao = int(input())

        if interacao == 1:
            cls.criar_paciente()
        if interacao == 2:
            cls.listar_pacientes()
        if interacao == 3:
            cls.deletar_paciente()
        if interacao == 4:
            cls.alterar_paciente()
        
        return interacao
    
    @classmethod
    def criar_paciente(cls):
        nome = input("informe o nome: ")
        cpf = input("informe o cpf: ")
        telefone = input("informe o telefone: ")
        ano = int(input("informe o ano: "))
        mes = int(input("informe o mês: "))
        dia = int(input("informe o dia: "))
        cls.pacientes.append(Paciente(nome, cpf, telefone, datetime(ano, mes, dia)))

    @classmethod
    def listar_pacientes(cls):
        for paciente in cls.pacientes:
            print(f"- paciente\n{paciente}\n- idade\n{paciente.idade()}")
        
    @classmethod
    def deletar_paciente(cls):
        cpf = input("informe o cpf: ")
        for paciente in cls.pacientes:
            if paciente.get_cpf() == cpf:
                cls.pacientes.remove(paciente)
                break

    @classmethod
    def alterar_paciente(cls):
        cls.deletar_paciente()
        cls.criar_paciente()
        
PacienteUI.main()