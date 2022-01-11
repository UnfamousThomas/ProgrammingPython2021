import math
fail = open("raamatud.txt", encoding="UTF-8")

kirjandus_tabel = [] # Tühi järjend, kuhu lisame raamatud

for rida in fail:    # Iga rea jaoks failist
    raamat = []     # Kogume reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    osad = rida.split(":") # Jupitame rea semikooloni koha pealt

    pealkiri = osad[0].strip() # Eraldame pealkirja
    leheküljed = int(osad[1].strip()) # Eraldame lehekülgede arvu

    raamat.append(pealkiri) # Lisame reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    raamat.append(leheküljed)

    kirjandus_tabel.append(raamat) # Lisame raamatute järjendi kirjanduse tabelisse

fail.close()

lugemiskiirus_uks_leht_minutites = 2
aega_lugeda_paevas_tundides = 2

total_age = 0

print("Raamatud, mille lugemiseks kulub rohkem kui neli päeva:")
for element in kirjandus_tabel:
    raamatuke = kirjandus_tabel[kirjandus_tabel.index(element)]
    lugemis_minutid = (int(raamatuke[1]) * lugemiskiirus_uks_leht_minutites)
    lugemis_tunnid = lugemis_minutid / 60
    total_age = total_age + lugemis_tunnid
    lugemis_paevad = math.ceil(lugemis_tunnid / 2)

    if(lugemis_paevad > 4):
        print(raamatuke[0] + " - " + str(lugemis_paevad) + " päeva")

print("Kõigi raamatute lugemiseks kulub " + str(round(total_age,1)) + "h.")

