n = int(input())
m = 9000
while True:
    n += 1
    if len(set(str(n))) == 4:
        break
print(n)
