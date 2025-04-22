print("Informe o número do mês")
numero = int(input())
if numero < 4:
    trimestre = "primeiro"
elif 3 < numero < 7:
    trimestre = "segundo"
elif 6 < numero < 10:
    trimestre = "terceiro"
elif 9 < numero < 13:
    trimestre = "quarto"
mes = {
    "1": "janeiro",
    "2": "fevereiro",
    "3": "março",
    "4": "abril",
    "5": "maio",
    "6": "junho",
    "7": "julho",
    "8": "agosto",
    "9": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro",
}
print(f"O mês de {mes[str(numero)]} é do {trimestre} trimestre do ano")