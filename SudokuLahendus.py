def kastid_korras(maatriks):
    # Vaatame igat 3x3 kasti
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            # Iga kasti korral kogume tema elemendid järjendisse 'kast'
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(maatriks[rea_nurk + i][veeru_nurk + j]))
            # Ja kontrollime, kas elemendid on korrektsed
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

failinimi = input("Sisesta faili nimi.")
fail = open(failinimi, encoding="UTF-8")
