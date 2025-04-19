while True:
    nota_primeiro = int(input("Digite a nota do primeiro bimestre da disciplina:\n"))
    if not (0 <= nota_primeiro <= 100):
        print("Número inválido, insira um valor inteiro entre 0 e 100")
    else:
        break
while True:
    nota_segundo = int(input("Digite a nota do primeiro bimestre da disciplina:\n"))
    if not (0 <= nota_segundo <= 100):
        print("Número inválido, insira um valor inteiro entre 0 e 100")
    else:
        break
print(f"Média parcial = {int((nota_primeiro * 2 + nota_segundo * 3) / 5)}")