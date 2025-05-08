n1, n2, n3 = map(int, input("Digite três números inteiros separados por espaços\n").split())

soma_pares = 0
for num in [n1, n2, n3]:
    if num % 2 == 0:
        soma_pares += num

print(f"Soma dos pares: {soma_pares}")