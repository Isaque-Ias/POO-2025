import math

class Circulo:
  def __init__(self):
    self._raio = 0
  
  def get_raio(self):
    return self._raio

  def set_raio(self, raio):
    self._raio = raio

  def calc_area(self):
    return math.pi * self._raio ** 2

  def calc_circumferencia(self):
    return 2 * math.pi * self._raio

meu_circulo = Circulo()
meu_circulo.set_raio(5)
print("Raio:", meu_circulo.get_raio())
print("Área:", f"{meu_circulo.calc_area():.3f}")
print("Circumferência:", f"{meu_circulo.calc_circumferencia():.3f}")