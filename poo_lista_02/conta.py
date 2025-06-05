class Conta:
    def __init__(self):
        self._titular = ""
        self._numero = "0000000000-0"
        self._saldo = 0
    
    def set_titular(self, titular):
        self._titular = titular

    def get_titular(self):
        return self._titular

    def set_numero(self, numero):
        self._numero = numero

    def get_numero(self):
        return self._numero

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor > self._saldo:
            print("O valor do saque supera o do saldo.")
        else:
            self._saldo -= valor

minha_conta = Conta()
minha_conta.set_titular("Fulano da Silva")
minha_conta.set_numero("0123456789-0")
print("Titular:", minha_conta.get_titular())
print("Número:", minha_conta.get_numero())
print("Saldo:", minha_conta.get_saldo(), "reais")
print("> Depósito de 30 reais")
minha_conta.depositar(30)
print("Saldo:", minha_conta.get_saldo(), "reais")
print("> Saque de 20 reais")
minha_conta.sacar(20)
print("Saldo:", minha_conta.get_saldo(), "reais")
print("> Saque de 15 reais")
minha_conta.sacar(15)
print("Saldo:", minha_conta.get_saldo(), "reais")

"""
DIAGRAMA UML

Conta
- titular : string
- numero : string
- saldo : double
+ Conta()
+ set_titular(t : string) : void
+ set_numero(n : string) : void
+ get_titular() : string
+ get_numero() : string
+ get_saldo() : double
+ depositar(v : double) : void
+ sacar(v : double) : void
"""