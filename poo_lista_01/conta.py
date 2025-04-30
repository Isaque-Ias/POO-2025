class Conta:
    def __init__(self):
        self.titular = 0
        self.numero = "0000000000-0"
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("O valor do saque supera o do saldo.")
        else:
            self.saldo -= valor

minha_conta = Conta()
minha_conta.titular = "Fulano da Silva"
minha_conta.numero = "0123456789-0"
print("Titular:", minha_conta.titular)
print("Número:", minha_conta.numero)
print("Saldo:", minha_conta.saldo, "reais")
print("> Depósito de 30 reais")
minha_conta.depositar(30)
print("Saldo:", minha_conta.saldo, "reais")
print("> Saque de 20 reais")
minha_conta.sacar(20)
print("Saldo:", minha_conta.saldo, "reais")
print("> Saque de 15 reais")
minha_conta.sacar(15)
print("Saldo:", minha_conta.saldo, "reais")