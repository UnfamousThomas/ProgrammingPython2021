def average(lst):
    return sum(lst) / len(lst)

def keskmised(jarjend):
    keskmised_list = []
    for aine in jarjend:
        ainenimi = aine[0]
        keskmine = round(average(aine[1:len(aine)]),1)
        list = [ainenimi, keskmine]
        keskmised_list.append(list)
    return keskmised_list

keskmised([['eesti keel', 5, 4, 3, 4, 4, 3, 4, 4],
               ['matemaatika', 4, 4, 5, 5, 4, 5, 5, 4, 5],
               ['keemia', 4, 3, 3, 2, 3, 4]])