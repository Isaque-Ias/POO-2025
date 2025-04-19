a, b, c = map(float, input().split(" "))
delta = b ** 2 - 4 * a * c
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    print(f"R1 = {((-b + delta ** 0.5) / (2 * a)):.5f}")
    print(f"R2 = {((-b - delta ** 0.5) / (2 * a)):.5f}")