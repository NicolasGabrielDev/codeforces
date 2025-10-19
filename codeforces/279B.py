n, t = input().split()
n, t = int(n), int(t)
books = list(map(int, input().split()))
dic = { 0: books[0] }

i = 1
while i < n:
    dic[i] = dic[i - 1] + books[i]
    
    i += 1
print(dic)