tamanho = int(input())
valores = [0, 1]
for i in range(tamanho - 2):
    valores.append(valores[i] + valores[i + 1])

valores = valores[0:tamanho]
valores = str(valores).replace(",", "")
print(valores[1:-1])
