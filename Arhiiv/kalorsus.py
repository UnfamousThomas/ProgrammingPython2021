fail = open("kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail: # iga rea jaoks failist
    korra_grammid = [] # kogume ühe toidukorra info
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korra_grammid.append(int(osa)) # järjekordne info juurde

    toitude_tabel.append(korra_grammid) # toidukorra järjend juurde

fail.close()

summa = 0
for element in toitude_tabel:
    toit = toitude_tabel[toitude_tabel.index(element)]
    susivesik = int(toit[0]) * 4
    valgud = int(toit[1]) * 4
    rasv = int(toit[2]) * 9
    summa = summa + susivesik + valgud + rasv

print(summa)