n_meninos = int(input())
meninos = list(map(int, input().split()))

n_meninas = int(input())
meninas = list(map(int, input().split()))

meninas.sort()
meninos.sort()

qtd = 0
i = 0
j = 0
while i < n_meninos and j < n_meninas:
    if abs(meninos[i] - meninas[j]) <= 1:
        qtd += 1
        i +=1 
        j += 1
    elif meninos[i] < meninas[j]:
        i += 1
    else:
        j += 1
        
print(qtd)