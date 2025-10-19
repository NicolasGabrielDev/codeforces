n = int(input())
q = 0
for _ in range(n):
    x = int(input())
    if 10 <= x <= 20:
        q += 1
print(f"{q} in")
print(f"{n - q} out")