fail = open("retseptid.txt", encoding="UTF-8")

retseptid_tabel = [] # Tühi järjend, kuhu lisame retseptid

for rida in fail:    # Iga rea jaoks failist
    koostisosad = []     # Kogume reas olevad koostisosad järjendisse
    osad = rida.split(",") # Jupitame rea koma koha pealt

    for osa in osad: # Vaatame iga juppi eraldi
        koostisosad.append(osa.strip()) # Lisame reas olevad koostisosad järjendisse

    retseptid_tabel.append(koostisosad) # Lisame koostisosade järjendi retseptide tabelisse

fail.close()

for element in retseptid_tabel:
    koostised = retseptid_tabel[retseptid_tabel.index(element)]
    if "suhkur" in koostised:
        if "maasikad" in koostised:
            print(koostised)