class Viagem:
    def __init__(self):
        self._distancia = 0
        self._tempo_horas = 0
        self._tempo_minutos = 0

    def set_distancia(self, distancia):
        self._distancia = distancia

    def get_distancia(self):
        return self._distancia

    def set_tempo(self, tempo):
        self._tempo_horas = tempo // 60
        self._tempo_minutos = tempo % 60

    def get_tempo(self, escala):
        if escala == "horas":
            return self._tempo_horas
        return self._tempo_minutos

    def calc_velocidade_media(self):
        return self._distancia / (self._tempo_horas + self._tempo_minutos / 60)

minha_viagem = Viagem()
minha_viagem.set_distancia(100)
minha_viagem.set_tempo(150)
print("Distância:", f"{minha_viagem.get_distancia()}km")
print("Tempo:", minha_viagem.get_tempo("horas"), "horas e", minha_viagem.get_tempo("minutos"), "minutos")
print("Velocidade média:", f"{minha_viagem.calc_velocidade_media():.0f}km/h")