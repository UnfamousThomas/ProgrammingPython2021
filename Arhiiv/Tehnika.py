fail = open("tehnika.txt", encoding="UTF-8")

for rida in fail:  # Iga rea jaoks failist
    eseme_tabel = rida.split(" ")
    algne_number = int(eseme_tabel[1])
    viimane_number = int(eseme_tabel[7])
    vahe = viimane_number - algne_number
    if vahe > 10:
        print(str(eseme_tabel[0]) + " - " + str(vahe) + "%")

fail.close()