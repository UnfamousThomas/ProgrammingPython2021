def symbolite_sagedus(tekst):
    syn = {}
    for c in tekst:
        if c in syn:
            syn[c] += 1
        else:
            syn[c] = 1
    return syn

print(symbolite_sagedus("suitsupääsuke"))
