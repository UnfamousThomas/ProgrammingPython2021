def kala_kaal(kala_pikkus, tusedus):
    kaal = (kala_pikkus * kala_pikkus * kala_pikkus) * tusedus / 100
    return round(kaal)

filename = str(input("Sisesta faili nimi."))
alam_moot = int(input("Sisesta kasutaja püügi alammõõt."))
fultoni_tusedus = float(input("Sisesta tüsedusindeks."))

fail = open(filename)
kaalud = []

for rida in fail:
    pikkus = int(rida)
    if pikkus < alam_moot:
        print("Kala lasti vette tagasi")
    else:
        kaal = kala_kaal(pikkus, fultoni_tusedus)
        kaalud.append((kaal / 1000))
        print(kaal)

suurim = max(kaalud)

print(suurim)

fail.close()