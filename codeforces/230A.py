#https://codeforces.com/problemset/problem/230/A

s, n = input().split()
s, n = int(s), int(n)

dic = {}
for _ in range(n):
    ds, db = input().split()
    ds, db = int(ds), int(db)
    if ds in dic:
        dic[ds].append(db)
    else:
        dic[ds] = [db]

flag = False
keys = sorted(dic.keys())
for k in keys:
    for db in dic[k]:
        if k < s:
            s += db
        else:
            flag = True
if flag:
    print("NO")
else:
    print("YES")
