# https://codeforces.com/problemset/problem/750/A

n, k = input().split()
n, k = int(n), int(k)

time = 60 * 4
time -= k

total = 0
i = 1
while time - i * 5 >= 0 and total < n:
    time -= i * 5
    i += 1
    total += 1
    
print(total)