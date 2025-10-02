v = 0
notas = 0.0
while v < 2:
    x = float(input())
    if x < 0.0 or x > 10.0:
        print("nota invalida")
    else:
        v += 1
        notas += x
print(f"media = {(notas / 2):.2f}")