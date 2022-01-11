fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail: # iga rea jaoks failist
    seti_punktid = [] # kogume ühe seti punkte
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        seti_punktid.append(int(osa)) # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid) # seti punktide järjend juurde
fail.close()

eesti_final = 0
soome_final = 0
for element in tulemuste_tabel:
    seti_punkt = tulemuste_tabel[tulemuste_tabel.index(element)]
    if seti_punkt[0] > seti_punkt[1]:
        eesti_final = eesti_final + 1
    elif seti_punkt[0] < seti_punkt[1]:
        soome_final = soome_final + 1

if eesti_final > soome_final:
    print("Eesti võitis " + str(eesti_final) + "-" + str(soome_final))
elif soome_final > eesti_final:
    print("Soome võitis " + str(soome_final) + "-" + str(eesti_final))
else:
    print("Mitte keegi ei võitnud.")
