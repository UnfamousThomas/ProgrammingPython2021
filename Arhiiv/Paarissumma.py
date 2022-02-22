def paarissumma(taisarv):
    if taisarv <= 1:
        return 0
    elif (taisarv % 2 != 0):
        return paarissumma(taisarv - 1)
    else:
        return taisarv + paarissumma(taisarv - 2)

print(paarissumma(101))