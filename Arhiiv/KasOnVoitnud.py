def voitis_nurkademangu(maatriks):
    if maatriks[0][0] == "X":
        if maatriks[0][4] == "X":
            if maatriks[4][0] == "X":
                if maatriks[4][4] == "X":
                    return True
    return False

def x_peadiagonaalil(maatriks):

    i = 0
    X_diagonaalil = 0
    for list in maatriks:
        if list[i] == "X":
            X_diagonaalil = X_diagonaalil + 1
        i = i + 1

    return X_diagonaalil;

def x_korvaldiagonaalil(maatriks):
    i = 4
    X_diagonaalil = 0
    for list in maatriks:
        if list[i] == "X":
            X_diagonaalil = X_diagonaalil + 1
        i = i - 1

    return X_diagonaalil

def voitis_diagonaalidemangu(maatriks):

    if x_korvaldiagonaalil(maatriks) == 5 and x_peadiagonaalil(maatriks) == 5:
        return True
    else:
        return False

def voitis_taismangu(maatriks):
    kogu_arv = 5*5
    asjade_arv = 0
    i = 0
    for line in maatriks:
        for el in line:
            if el == "X":
                asjade_arv = asjade_arv + 1
    if asjade_arv == kogu_arv:
        return True
    else:
        return False

maatriks =    \
    [['X', 'X', 'X', 'X', 'X'], # [0][4]
    ['X', 'X', 'X', 'X', 'X'], # [1][3]
    ['X', 'X', 'X', 'X', 'X'], # [2][2]
    ['X', 'X', 'X', 'X', 'X'], # [3] [1]
    ['X', 'X', 'X', 'X', 'X']] # [4] [0]

voitis_diagonaalidemangu(maatriks)