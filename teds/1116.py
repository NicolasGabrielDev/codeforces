n = int(input())
for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)

    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{(x / y):.1f}")