maior = 0
maior_index = -1
i = 1
while i <= 100:
    valor = int(input())
    if valor > maior:
        maior = valor
        maior_index = i

print(maior)
print(maior_index)