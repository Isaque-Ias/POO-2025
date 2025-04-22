print("Digite o primeiro horário no formato hh:mm")
primeira_hora = list(map(int, input().split(":")))
print("Digite o segundo horário no formato hh:mm")
segunda_hora = list(map(int, input().split(":")))
total_minutos = (primeira_hora[1] + segunda_hora[1]) % 60
total_horas = primeira_hora[0] + segunda_hora[0] + (1 if primeira_hora[1] + segunda_hora[1] >= 60 else 0)
print(f"Total de horas = {'0' if total_horas < 10 else ''}{total_horas}:{'0' if total_minutos < 10 else ''}{total_minutos}")