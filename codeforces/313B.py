# https://codeforces.com/problemset/problem/313/B

s = input()
q = int(input())

i = 0
aux = ''
aux_n = 0
dic = {}
for c in s:
    if i == 0:
        aux = c
    else:
        if c == aux:
            aux_n += 1
        else:
            aux = c
    dic[i] = aux_n
    i += 1

for _ in range(q):
    a, b = input().split()
    a, b = int(a), int(b)
    print(dic[b - 1] - dic[a - 1])