a, b = map(int, input().split(" "))
if -500 <= a <= 500 and -500 <= b <= 500:
    print("dentro" if 0 <= a <= 432 and 0 <= b <= 468 else "fora")
else:
    print("Presentation Error")