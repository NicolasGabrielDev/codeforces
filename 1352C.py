# https://codeforces.com/problemset/problem/1352/C

t = int(input())
for _ in range(t):
    n, k = input().split()
    n, k = int(n), int(k)
    
    q = k // (n - 1)
    r = k % (n - 1)
    
    if r == 0:
        print(q * n - 1)
    else:
        print(q * n + r)
    
