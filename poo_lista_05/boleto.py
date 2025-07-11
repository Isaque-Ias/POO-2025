from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, codigo, emissao, vencimento, valor):
        self.set_codigo(codigo)
        self.set_emissao(emissao)
        self.set_vencimento(vencimento)
        self.set_valor(valor)

        self.data_pagamento = None
        self.situacao_pagamento = Pagamento.EM_ABERTO
        self.valor_pago = 0

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo
        if not codigo.isalpha():
            raise ValueError()

    def get_emissao(self):
        return self.emissao

    def set_emissao(self, emissao):
        self.emissao = emissao

    def get_vencimento(self):
        return self.vencimento
    
    def set_vencimento(self, vencimento):
        self.vencimento = vencimento

    def get_valor(self):
        return self.valor

    def set_valor(self, valor):
        if not isinstance(valor, int):
            raise ValueError()
        self.valor = valor

    def pagar(self, valor):
        if not isinstance(valor, int):
            raise ValueError()

        if valor > self.valor - self.valor_pago:
            raise ValueError("O pagamento é maior que o valor a pagar do boleto")
        
        self.valor_pago += valor
        self.data_pagamento = datetime.now()
        if self.valor_pago == self.valor:
            self.situacao_pagamento = Pagamento.PAGO
        else:
            self.situacao_pagamento = Pagamento.PAGO_PARCIAL

    def situacao(self):
        return self.situacao_pagamento

    def __str__(self):
        return f"codigo: {self.get_codigo()}, emissao: {self.get_emissao()}, vencimento: {self.get_vencimento()}, valor: {self.get_valor()}"

class BoletoUI:
    boletos = []

    @classmethod
    def main(cls):
        while True:
            interacao = cls.menu()
            if interacao == 5:
                break

    @classmethod
    def menu(cls):
        print("1 - cadastrar boleto\n2 - ver boletos\n3 - pagar boleto\n4 - situacao boleto\n5 - sair")
        interacao = int(input())

        if interacao == 1:
            cls.criar_boleto()
        if interacao == 2:
            cls.listar_boletos()
        if interacao == 3:
            cls.pagar_boleto()
        if interacao == 4:
            cls.situacao_boleto()
        
        return interacao
    
    @classmethod
    def criar_boleto(cls):
        codigo = input("informe o codigo: ")
        emissao_ano = int(input("informe o ano da emissão: "))
        emissao_mes = int(input("informe o mês da emissão: "))
        emissao_dia = int(input("informe o dia da emissão: "))
        emissao_data = datetime(emissao_ano, emissao_mes, emissao_dia)
        if emissao_mes > 9:
            vencimento_data = datetime(emissao_ano + 1, emissao_mes - 9, emissao_dia)
        else:
            vencimento_data = datetime(emissao_ano, emissao_mes + 3, emissao_dia)
        valor = int(input("informe o valor: "))
        cls.boletos.append(Boleto(codigo, emissao_data, vencimento_data, valor))

    @classmethod
    def listar_boletos(cls):
        for boleto in cls.boletos:
            print(boleto)
        
    @classmethod
    def pagar_boleto(cls):
        codigo = input("informe o codigo: ")
        valor = int(input("informe o valor: "))
        for boleto in cls.boletos:
            if boleto.get_codigo() == codigo:
                boleto.pagar(valor)
                break

    @classmethod
    def situacao_boleto(cls):
        codigo = input("informe o codigo: ")
        for boleto in cls.boletos:
            if boleto.get_codigo() == codigo:
                print(boleto.situacao())
                break
        
BoletoUI.main()

# Escreva a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo.
# • A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores
# e situação de pagamento;
# • O construtor da classe recebe os dados iniciais de um boleto;
# • O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto;
# • O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento
# ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o
# valor do pagamento corresponder ao valor do boleto;
# • O método ToString deve retornar um texto com os atributos do objeto;
# • A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
# • Inclua métodos de acesso na classe para permitir alterar e recuperar os dados de um boleto (não apresentados
# no diagrama;
# • Faça uma UI para testar a classe e a enumeração.