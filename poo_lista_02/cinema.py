class Ingresso:
   def __init__(self):
      self._dia = "segunda"
      self._horario_horas = 0
      self._horario_minutos = 0

   def set_dia(self, dia):
      self._dia = dia
   
   def get_dia(self):
      return self._dia

   def set_horario_horas(self, horas):
      self._horario_horas = horas
   
   def get_horario_horas(self):
      return self._horario_horas
   
   def set_horario_minutos(self, minutos):
      self._horario_minutos = minutos
   
   def get_horario_minutos(self):
      return self._horario_minutos
   
   def valor_da_entrada_inteira(self):
      if self._dia in ["segunda", "terça", "quinta"]:
         base = 16
      elif self._dia == "quarta":
         base = 8
      else:
         base = 20
         if self._horario_horas > 17:
            base *= 1.5
            base = int(base)
      return base

   def valor_da_entrada_meia(self):
      if self._dia in ["segunda", "terça", "quinta"]:
         base = 8
      elif self._dia == "quarta":
         base = 8
      else:
         base = 10
         if self._horario_horas > 17:
            base *= 1.5
            base = int(base)
      return base

meu_ingresso_a = Ingresso()
meu_ingresso_a.set_dia("sábado")
meu_ingresso_a.set_horario_horas(14)
meu_ingresso_a.set_horario_minutos(30)

print("Ingresso 1")
print("Dia:", meu_ingresso_a.get_dia())
print("Horário:", meu_ingresso_a.get_horario_horas(), "horas e", meu_ingresso_a.get_horario_minutos(), "minutos")
print("Inteira:", meu_ingresso_a.valor_da_entrada_inteira(), "| Meia", meu_ingresso_a.valor_da_entrada_meia())

meu_ingresso_b = Ingresso()
meu_ingresso_b.set_dia("sexta")
meu_ingresso_b.set_horario_horas(19)
meu_ingresso_b.set_horario_minutos(30)

print("Ingresso 2")
print("Dia:", meu_ingresso_b.get_dia())
print("Horário:", meu_ingresso_b.get_horario_horas(), "horas e", meu_ingresso_b.get_horario_minutos(), "minutos")
print("Inteira:", meu_ingresso_b.valor_da_entrada_inteira(), "| Meia", meu_ingresso_b.valor_da_entrada_meia())

meu_ingresso_c = Ingresso()
meu_ingresso_c.set_dia("quarta")
meu_ingresso_c.set_horario_horas(16)
meu_ingresso_c.set_horario_minutos(0)

print("Ingresso 3")
print("Dia:", meu_ingresso_c.get_dia())
print("Horário:", meu_ingresso_c.get_horario_horas(), "horas e", meu_ingresso_c.get_horario_minutos(), "minutos")
print("Inteira:", meu_ingresso_c.valor_da_entrada_inteira(), "| Meia", meu_ingresso_c.valor_da_entrada_meia())

"""
DIAGRAMA UML

Cinema
- dia : string
- horario_horas : double
- horario_minutos : double
+ Cinema()
+ set_dia(d : string) : void
+ set_horario_horas(h : double) : void
+ set_horario_minutos(m : double) : void
+ get_dia() : string
+ get_horario_horas() : double
+ get_horario_minutos() : double
+ valor_da_entrada_inteira() : double
+ valor_da_entrada_meia() : double
"""