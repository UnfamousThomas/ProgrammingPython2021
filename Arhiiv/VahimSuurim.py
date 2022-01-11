def vahimatest_suurim(tais_maatriks):
    vahimad_elemendid = []
    for element in tais_maatriks:
        vaikseim = min(element)
        vahimad_elemendid.append(vaikseim)

    return max(vahimad_elemendid)