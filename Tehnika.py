##Võrdle viimane ja esimene number
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


def get_Percentage(amount, total):
    osakal = amount / total
    return osakal * 100


fail = open("tehnika.txt", encoding="UTF-8")

tehnika_tabel = []  # Tühi järjend, kuhu lisame raamatud

for rida in fail:  # Iga rea jaoks failist
    rea_list = rida.split(" ")
    tehnika = [rea_list[0]]
    for num in rea_list[1:len(rea_list)]:
        tehnika.append(int(num))
    tehnika_tabel.append(tehnika)

suur_kasv = []
summa = 0

for tehnika in tehnika_tabel:
    print(get_change(tehnika[6], tehnika[1]))
#     if get_change(tehnika[6], tehnika[1]) >= 10:
#         suur_kasv.append(tehnika)
#         summa = summa + tehnika[len(tehnika)-1]
#
# for tehnika in suur_kasv:
#     print(suur_kasv[0][0] + " - " + str(get_Percentage(suur_kasv[0][6], summa)))

fail.close()
