print("Digite quatro valores inteiros")
pares = 0
impares = 0
for _ in range(4):
    valor = int(input())
    valor_modulado = valor % 2
    if(valor_modulado == 1):
        pares += valor
    else:
        impares += valor
print(f"Soma dos pares = {pares}")
print(f"Soma dos ímpares = {impares}")