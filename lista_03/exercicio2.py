
a = input()
b = input()

passed_a = False
dot_a = a.find(".") + 1
if (not dot_a == 0) and len(a) - dot_a == 1 and 0 <= float(a) <= 10:
    passed_a = True

passed_b = False
dot_b = b.find(".") + 1
if (not dot_b == 0) and len(b) - dot_b == 1 and 0 <= float(b) <= 10:
    passed_b = True
    
if passed_a and passed_b:
    a = float(a)
    b = float(b)
    print(f"MEDIA = {((a * 3.5 + b * 7.5) / 11):.5f}")
else:
    print("Presentation Error")