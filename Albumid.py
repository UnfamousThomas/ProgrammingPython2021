from collections import OrderedDict
def loo_album(list):
    uus_list = []
    uus_list.append(list[0])
    uus_list.append(list[1])
    uus_list.append(list[2])
    uus_list.append(list[3].replace("\n", ""))

    return uus_list

def sorteeri(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    syn = {}
    for rida in fail:
        rida_list = rida.split(";")

        aasta = rida_list[2]
        aasta_esimesed_2_arvu = aasta[0] + aasta[1]
        indeks = aasta_esimesed_2_arvu + aasta[2] + "0"
        if indeks not in syn:
            uus_suur_list = [loo_album(rida_list)]
            syn[int(indeks)] = uus_suur_list
        else:
            suur_list = syn[indeks]
            suur_list.append(loo_album(rida_list))
            syn[int(indeks)] = suur_list

    fail.close()
    return OrderedDict(sorted(syn.items(), key=lambda t: t[0]))

def kuva(sorteeritud):
    for year in sorteeritud:
        hetkel_list = []
        for list in sorteeritud[year]:
            if(len(hetkel_list) != 0):
                if(hetkel_list[2] < list[3]):
                    hetkel_list.clear()
                    hetkel_list.append(list[0])  # Nimi
                    hetkel_list.append(list[1])  # Album
                    hetkel_list.append(list[3])  # Müükide hulk
            else:
                hetkel_list.append(list[0]) # Nimi
                hetkel_list.append(list[1]) # Album
                hetkel_list.append(list[3]) # Müükide hulk
        print(str(year) + ": " + str(len(sorteeritud[year])) + " album(it) (" + str(hetkel_list[0]) + " - " + str(hetkel_list[1]) + ")")


kuva(sorteeri("albumid.txt"))
