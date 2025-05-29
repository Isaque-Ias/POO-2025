import math

class Retangulo:
    def __init__(self, b, h):
        if b <= 0 or h <= 0:
            raise ValueError("Base e altura devem ser valores positivos.")
        self.__base = b
        self.__altura = h

    def SetBase(self, b):
        if b > 0:
            self.__base = b
        else:
            raise ValueError("A base deve ser um valor positivo.")

    def SetAltura(self, h):
        if h > 0:
            self.__altura = h
        else:
            raise ValueError("A altura deve ser um valor positivo.")

    def GetBase(self):
        return self.__base

    def GetAltura(self):
        return self.__altura

    def CalcArea(self):
        return self.__base * self.__altura

    def CalcDiagonal(self):
        return math.sqrt(self.__base ** 2 + self.__altura ** 2)

    def ToString(self):
        return (f"Retângulo:\n"
                f"Base = {self.__base}\n"
                f"Altura = {self.__altura}\n"
                f"Área = {self.CalcArea():.2f}\n"
                f"Diagonal = {self.CalcDiagonal():.2f}")

meu_retangulo = Retangulo(20, 30)
print(meu_retangulo.ToString())