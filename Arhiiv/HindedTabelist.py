import statistics
fail = open("hinded.csv", encoding="UTF-8")

hinde_tabel = [] # Tühi järjend, kuhu lisame raamatud

for rida in fail:    # Iga rea jaoks failist
    rea_list = rida.split(",")
    hinne = []

    hinne.append(rea_list[0])
    for num in rea_list[1:len(rea_list)]:
        hinne.append(float(num))
    hinde_tabel.append(hinne)
fail.close()

for hinne in hinde_tabel:
    aine = hinne[0]
    keskmine = round(statistics.mean(hinne[1:len(hinne)]),1)
    print(aine + ": " + str(keskmine))
