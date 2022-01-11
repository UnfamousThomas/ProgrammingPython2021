failinimi = input("Sisesta failinimi")

fail = open(failinimi)

rea_numbrid = []

i = 1
for rida in fail:
    numbrid_string = rida.split(" ")
    numbrid_int = []
    for num in numbrid_string:
        numbrid_int.append(int(num))
    summa = sum(numbrid_int)
    paris_list = [i, summa]
    rea_numbrid.append(paris_list)
    i = 1 + i
fail.close()

summad = []
for rida in rea_numbrid:
    summad.append(rida[1])

suurim = max(summad)

for rida in rea_numbrid:
    if rida[1] == suurim:
        print("Suurim summa on failis " + str(rida[0]) + ". real ja see on " + str(suurim) + ".")

