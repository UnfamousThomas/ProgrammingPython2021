fail = open("maalahedane.csv", encoding="UTF-8")

maa_tabel = []
numbrid_tabel = []
for rida in fail:  # Iga rea jaoks failist
    rea_list = rida.split(";")
    maa = []
    numbrid = []
    maa.append(rea_list[0])
    for num in rea_list[1:len(rea_list)]:
        numbrid.append(int(num))
    numbrid_summa = sum(numbrid)
    maa.append(numbrid_summa)
    numbrid_tabel.append(numbrid_summa)
    maa_tabel.append(maa)
fail.close()

suurim_num = max(numbrid_tabel)
for maa in maa_tabel:
    if maa[1] == suurim_num:
        print("Kõige rohkem osalejaid - " + str(maa[0]) + ", " + str(suurim_num) + " inimest.")
        print("Kokku on kursusel osalenud " + str(sum(numbrid_tabel)) + " inimest.")
