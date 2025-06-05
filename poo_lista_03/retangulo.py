import math

class Retangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("Base e altura devem ser valores positivos.")
        self._base = base
        self._altura = altura

    def SetBase(self, base):
        if base <= 0:
            raise ValueError("A base deve ser positiva.")
        self._base = base

    def SetAltura(self, altura):
        if altura <= 0:
            raise ValueError("A altura deve ser positiva.")
        self._altura = altura

    def GetBase(self):
        return self._base

    def GetAltura(self):
        return self._altura

    def CalcArea(self):
        return self._base * self._altura

    def CalcDiagonal(self):
        return math.sqrt(self._base ** 2 + self._altura ** 2)

    def ToString(self):
        return (f"Retângulo:\n"
                f"Base: {self._base}\n"
                f"Altura: {self._altura}\n"
                f"Área: {self.CalcArea():.2f}\n"
                f"Diagonal: {self.CalcDiagonal():.2f}")
