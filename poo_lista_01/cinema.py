class Ingresso:
    def __init__(self):
        self.dia = "segunda"
        self.horario_horas = 0
        self.horario_minutos = 0
    
    def valor_da_entrada_inteira(self):
        if self.dia in ["segunda", "terça", "quinta"]:
           base = 16
        elif self.dia == "quarta":
           base = 8
        else:
           base = 20
           if self.horario_horas > 17:
              base *= 1.5
              base = int(base)
        return base

    def valor_da_entrada_meia(self):
        if self.dia in ["segunda", "terça", "quinta"]:
           base = 8
        elif self.dia == "quarta":
           base = 8
        else:
           base = 10
           if self.horario_horas > 17:
              base *= 1.5
              base = int(base)
        return base

meu_ingresso_a = Ingresso()
meu_ingresso_a.dia = "sábado"
meu_ingresso_a.horario_horas = 14
meu_ingresso_a.horario_minutos = 30

print("Ingresso 1")
print("Dia:", meu_ingresso_a.dia)
print("Horário:", meu_ingresso_a.horario_horas, "horas e", meu_ingresso_a.horario_minutos, "minutos")
print("Inteira:", meu_ingresso_a.valor_da_entrada_inteira(), "| Meia", meu_ingresso_a.valor_da_entrada_meia())

meu_ingresso_b = Ingresso()
meu_ingresso_b.dia = "sexta"
meu_ingresso_b.horario_horas = 19
meu_ingresso_b.horario_minutos = 30

print("Ingresso 2")
print("Dia:", meu_ingresso_b.dia)
print("Horário:", meu_ingresso_b.horario_horas, "horas e", meu_ingresso_b.horario_minutos, "minutos")
print("Inteira:", meu_ingresso_b.valor_da_entrada_inteira(), "| Meia", meu_ingresso_b.valor_da_entrada_meia())

meu_ingresso_c = Ingresso()
meu_ingresso_c.dia = "quarta"
meu_ingresso_c.horario_horas = 16
meu_ingresso_c.horario_minutos = 0

print("Ingresso 3")
print("Dia:", meu_ingresso_c.dia)
print("Horário:", meu_ingresso_c.horario_horas, "horas e", meu_ingresso_c.horario_minutos, "minutos")
print("Inteira:", meu_ingresso_c.valor_da_entrada_inteira(), "| Meia", meu_ingresso_c.valor_da_entrada_meia())