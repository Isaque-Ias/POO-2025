class Agua:
    def __init__(self, mes, ano, consumo):
        self.mes = mes
        self.ano = ano
        self.consumo = consumo
    
    def calcular_valor(self):
        valor = 38.00
        
        if self.consumo > 10 and self.consumo <= 20:
            valor += (self.consumo - 10) * 5
        
        elif self.consumo > 20:
            valor += (10 * 5) + (self.consumo - 20) * 6
        
        return valor

mes = int(input("Digite o mês da conta: "))
ano = int(input("Digite o ano da conta: "))
consumo = float(input("Digite o consumo em m³: "))

conta_agua = Agua(mes, ano, consumo)

valor_conta = conta_agua.calcular_valor()

print(f"O valor da conta de água para {mes}/{ano} com consumo de {consumo}m³ é R$ {valor_conta:.2f}")
