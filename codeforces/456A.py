n = int(input())
prices = []
dic = {}
for _ in range(n):
    price, quality = map(int, input().split())
    prices.append(price)
    dic[price] = quality
prices.sort()

flag = False
i = 1
while i < n:
    first = prices[i - 1]
    if dic[first] > dic[prices[i]]:
        flag = True
    i += 1
if flag:
    print("Happy Alex")
else:
    print("Poor Alex")