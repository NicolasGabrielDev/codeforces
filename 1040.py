n1, n2, n3, n4 = map(float, input().split())
s = n1 * 2 + n2 * 3 + n3 * 4 + n4
media = s / 10
print(f"Media: {media:.1f}")
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    nova_media = (media + exame) / 2
    if nova_media >= 5.0:
        print(f"Aluno aprovado.\nMedia final: {nova_media:.1f}")
    else:
        print("Aluno reprovado.")