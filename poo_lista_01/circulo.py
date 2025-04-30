import math

class Circulo:
  def __init__(self):
    self.raio = 0
  
  def calc_area(self):
    return math.pi * self.raio ** 2

  def calc_circumferencia(self):
    return 2 * math.pi * self.raio

meu_circulo = Circulo()
meu_circulo.raio = 5
print("Raio:", meu_circulo.raio)
print("Área:", f"{meu_circulo.calc_area():.3f}")
print("Circumferência:", f"{meu_circulo.calc_circumferencia():.3f}")