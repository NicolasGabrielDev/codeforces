t = int(input())
max_number = None
tests = []
numbers = []
for _ in range(t):
    x = int(input())
    if max_number == None:
        max_number = x
    elif max_number < x:
        max_number = x
    tests.append(x)
 
aux = 1
while True:
    r = aux ** 3
    if r > max_number:
        break
    
    numbers.append(r)
    aux += 1
 
size = len(numbers)
 
for t in tests:
    flag = False
    for a in numbers:
        if a + a == t:
            flag = True
            break
    if flag:
        print("YES")
        continue
    else:
        flag = False
        left = 0
        right = size - 1
        while left <= right:
            r = numbers[left] + numbers[right]
            if r == t:
                flag = True
                break
            if r < t:
                left += 1
            elif r > t:
                right -= 1
        if flag:
            print("YES")
        else:
            print("NO")
