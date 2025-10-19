n = int(input())

bacteria = []

i = 1
while True:
    if 2 ** i > n:
        break
    
    i += 1
    
remaining = 2 ** (i - 1)
if remaining == n:
    print(1)
else:
    print(1 + n - remaining)