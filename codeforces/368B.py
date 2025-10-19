# https://codeforces.com/problemset/problem/368/B

n, m = input().split()
n, m = int(n), int(m)
values = list(map(int, input().split()))
values.reverse()
dic = {}
conj = set()
for i, v in enumerate(values):
    if v not in conj:
        dic[i] = dic.get(i - 1, 0) + 1
        conj.add(v)
    else:
        dic[i] = dic[i - 1]
for _ in range(m):
    l = int(input())
    print(dic[n - l])