# https://codeforces.com/problemset/problem/466/A

n, m, a, b = input().split()
n, m, a, b = int(n), int(m), int(a), int(b)

max_mtickets = n // m

solutions = []

if n == 1:
    print(min(a, b))
else:
    i = 0
    while i <= n:
        value_mticket = i * b
        
        remaining = n - (i * m)
        value_regular_ticket = 0
        if remaining > 0:
            value_regular_ticket = remaining * a
        
        solutions.append(value_regular_ticket + value_mticket)
        
        
        i += 1
        
    print(min(solutions))