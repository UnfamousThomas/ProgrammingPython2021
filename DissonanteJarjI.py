def oppositeSigns(x, y):
    return ((x ^ y) < 0)

x = 100
y = -1

def on_rahulik(arvamus1, arvamus2, erinevus):
    #1 -4 = -3
    print(arvamus1)
    if abs(abs(arvamus1) - arvamus2) > erinevus or arvamus1 * arvamus2 == 0:
        if oppositeSigns(arvamus1, arvamus2):
            #print("Arvamus 1: " + str(arvamus1))
            #print("Arvamus 2: " + str(arvamus2))

            return False
    return True


def dissonantside_arv(arvamused, lubatud_erinevus):
    dissonantsid = 0

    i = 1
    while i <= (len(arvamused)):
        if not on_rahulik(arvamused[i-1], arvamused[i], lubatud_erinevus):
            dissonantsid += 1
        i = i + 2
    return dissonantsid


print(dissonantside_arv([1, -3, 1, 0, 0, -2, -3, 3, -3, 12], 3))
