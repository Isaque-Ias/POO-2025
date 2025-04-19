a = int(input())
b = int(input())
c = int(input())
if 0 <= a <= 1000 and 0 <= b <= 1000 and 0 <= c <= 1000:
    menor = 3001
    total_a = b + c * 2
    total_b = a + c
    total_c = a * 2 + b
    if total_a < total_b:
        if total_a < total_c:
            menor = total_a
        else:
            menor = total_c
    else:
        if total_b < total_c:
            menor = total_b
        else:
            menor = total_c

    print(menor * 2)
else:
    print("Presentation Error")