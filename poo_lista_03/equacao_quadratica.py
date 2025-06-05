import math

class EquacaoQuadratica:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("O coeficiente 'a' deve ser diferente de zero em uma equação do 2º grau.")
        self._a = a
        self._b = b
        self._c = c

    def SetA(self, a):
        if a == 0:
            raise ValueError("O coeficiente 'a' deve ser diferente de zero.")
        self._a = a

    def SetB(self, b):
        self._b = b

    def SetC(self, c):
        self._c = c

    def GetA(self):
        return self._a

    def GetB(self):
        return self._b

    def GetC(self):
        return self._c

    def Delta(self):
        return self._b**2 - 4*self._a*self._c

    def TemRaizesReais(self):
        return self.Delta() >= 0

    def Raiz1(self):
        if not self.TemRaizesReais():
            return None
        return (-self._b + math.sqrt(self.Delta())) / (2*self._a)

    def Raiz2(self):
        if not self.TemRaizesReais():
            return None
        return (-self._b - math.sqrt(self.Delta())) / (2*self._a)

    def ToString(self):
        return (f"Equação: {self._a}x² + {self._b}x + {self._c} = 0\n"
                f"Delta: {self.Delta():.2f}\n"
                f"Tem raízes reais? {'Sim' if self.TemRaizesReais() else 'Não'}\n"
                f"Raiz 1: {self.Raiz1() if self.Raiz1() is not None else 'N/A'}\n"
                f"Raiz 2: {self.Raiz2() if self.Raiz2() is not None else 'N/A'}")

"""
DIAGRAMA UML

EquacaoQuadratica
- a : double
- b : double
- c : double
+ EquacaoQuadratica(a : double, b : double, c : double)
+ SetA(a : double) : void
+ SetB(b : double) : void
+ SetC(c : double) : void
+ GetA() : double
+ GetB() : double
+ GetC() : double
+ Delta() : double
+ TemRaizesReais() : boolean
+ Raiz1() : double
+ Raiz2() : double
+ ToString() : string
"""