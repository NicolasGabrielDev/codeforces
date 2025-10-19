n = int(input())
for _ in range(n):
    a, b, c = map(float, input().split())
    s = a * 2 + b * 3 + c * 5
    print(f"{(s / 10):.1f}")