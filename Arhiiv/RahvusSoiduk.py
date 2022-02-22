def failist_sonastik(fail):
    fail = open(fail, encoding="UTF-8")
    syn = {}
    for rida in fail:
        elemendid = rida.split(" ")
        syn[elemendid[0]] = elemendid[1].replace("\n", "")
    fail.close()
    return syn

def tahised_nimedeks(jarjend, syn):
    tagastatav_jarjend = []

    for tahis in jarjend:
        if tahis not in syn:
            tagastatav_jarjend.append(None)
        else:
            tagastatav_jarjend.append(syn[tahis])
    return tagastatav_jarjend

failinimi = input("Sisestage andmebaasi faili nimi:")
piiri_soiduk = input("Sisestage Piiriületajad")

piiri_uletajad = piiri_soiduk.split(" ")

for nimi in tahised_nimedeks(piiri_uletajad, failist_sonastik(failinimi)):
    if nimi is None:
        print("Tundmatu maa")
    else:
        print(nimi)