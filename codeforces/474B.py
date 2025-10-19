# https://codeforces.com/problemset/problem/474/B

n = int(input())
arr_n = list(map(int, input().split()))
m = int(input())
arr_m = list(map(int, input().split()))

piles = {}

i = 1
j = 1
for a in arr_n:
    for _ in range(a):
        piles[i] = j
        i += 1
    j += 1

for b in arr_m:
    print(piles[b])