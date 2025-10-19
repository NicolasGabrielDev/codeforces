n = int(input())
l = map(int, input().split())
dic = {}
for v in l:
    dic[v] = dic.get(v, 0) + 1
    
print(dic)