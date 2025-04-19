total = int(input())
coelhos = 0
ratos = 0
sapos = 0
cobaias = 0
for i in range(total):
    valor, entidade = input().split(" ")
    valor = int(valor)
    if entidade == "C":
        coelhos += valor
    elif entidade == "R":
        ratos += valor
    elif entidade == "S":
        sapos += valor
    cobaias += valor
print(f"Total: {cobaias} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {(100 * coelhos / cobaias):.2f} %")
print(f"Percentual de ratos: {(100 * ratos / cobaias):.2f} %")
print(f"Percentual de sapos: {(100 * sapos / cobaias):.2f} %")