print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
media = (a + b + c + d) / 4
print(f"Média = {media}")
print("Números menores que a média")
if a < media:
    print(a)
if b < media:
    print(b)
if c < media:
    print(c)
if d < media:
    print(d)
print("Números maiores ou iguais à média")
if a >= media:
    print(a)
if b >= media:
    print(b)
if c >= media:
    print(c)
if d >= media:
    print(d)