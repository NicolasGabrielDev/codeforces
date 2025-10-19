hi, mi, hf, mf = input().split()
hi, mi, hf, mf = int(hi), int(mi), int(hf), int(mf)
if hi == mi == hf == mf:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    hj = hf - hi
    mj = mf - mi

    if mj < 0:
        hj -= 1
    mj = 60 + mj

    if hj < 0:
        hj = 24 + hj

    print(f"O JOGO DUROU {hj} HORA(S) E {mj} MINUTO(S)")