a, b = map(float, input().split(" "))
if a.is_integer and b.is_integer and 1 <= a <= 10 ** 8 and 1 <= b <= 100:
    print(int(a % b))
else:
    print("Presentation Error")