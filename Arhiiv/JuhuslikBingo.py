import random


def juhuslik_bingo():
    bingo_list = []
    i = 0
    for i in range(5):
        minimum_vaartus = i * 15 + 1
        maksimum_vaartus = (i + 1) * 15
        random_list = random.sample(range(minimum_vaartus, maksimum_vaartus), 5)
        bingo_list.append(random_list)
        i = i + 1

    zipped_rows = zip(*bingo_list)
    transpose_matrix = [list(row) for row in zipped_rows]

    return transpose_matrix


juhuslik_bingo()
