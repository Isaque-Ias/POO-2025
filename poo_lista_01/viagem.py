class Viagem:
    def __init__(self):
        self.distancia = 0
        self.tempo_horas = 0
        self.tempo_minutos = 0
    
    def calc_velocidade_media(self):
        return self.distancia / (self.tempo_horas + self.tempo_minutos / 60)

minha_viagem = Viagem()
minha_viagem.distancia = 100
minha_viagem.tempo_horas = 2
minha_viagem.tempo_minutos = 30
print("Distância:", f"{minha_viagem.distancia}km")
print("Tempo:", minha_viagem.tempo_horas, "horas e", minha_viagem.tempo_minutos, "minutos")
print("Velocidade média:", f"{minha_viagem.calc_velocidade_media():.3f}km/h")