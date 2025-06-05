class Frete:
    def __init__(self, distancia, peso):
        if distancia <= 0 or peso <= 0:
            raise ValueError("Distância e peso devem ser valores positivos.")
        self._distancia = distancia
        self._peso = peso

    def SetDistancia(self, distancia):
        if distancia <= 0:
            raise ValueError("A distância deve ser positiva.")
        self._distancia = distancia

    def SetPeso(self, peso):
        if peso <= 0:
            raise ValueError("O peso deve ser positivo.")
        self._peso = peso

    def GetDistancia(self):
        return self._distancia

    def GetPeso(self):
        return self._peso

    def CalcFrete(self):
        return self._peso * self._distancia * 0.01

    def ToString(self):
        return (f"Frete:\n"
                f"Distância: {self._distancia} km\n"
                f"Peso: {self._peso} kg\n"
                f"Valor do frete: R$ {self.CalcFrete():.2f}")
