def kas_Paaritu(number):
    if (number % 2) == 0:
        return False
    else:
        return True


def alla_ules(n):
    if n <= 0:
        print("Põhi!")
    else:
        print(n)
        alla_ules(n - 2)
        print(n - 1)


alla_ules(5)