x = int(input())
y = int(input())
if x > y:
    x, y = y, x

q = 0
x += 1
while x < y:
    if x % 2 == 1:
        q += x
    x += 1
print(q)