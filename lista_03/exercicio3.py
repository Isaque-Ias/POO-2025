import math as m

raio = float(input())
if raio >= 0:
    print(f"VOLUME = {(4 / 3 * m.pi * raio ** 3):.3f}")
else:
    print("Presentation Error")