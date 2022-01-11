def nummerda(korruste_arv, korterite_arv_korrusel):
    maja_list = []
    for korrus in range(korruste_arv):
        korruse_list = []
        for korter in range(korterite_arv_korrusel):
            korrus_num = korrus + 1
            korter_num = korter + 1
            korruse_list.append(str(korrus_num) + str(korter_num))
        maja_list.append(korruse_list)

    return maja_list
print(nummerda(3, 4))
