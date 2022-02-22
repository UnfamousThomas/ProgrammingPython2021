def kooslubajad (jarjend):
    tulemus = (0,0)
    makssuurus = -1
    for i in range(len(jarjend) - 1):
        for j in range(i+1, len(jarjend)):
            #print(jarjend[i])
            #print(jarjend[j])
            print(jarjend[i].difference(jarjend[j]))

kooslubajad([{"maamaks kaotada", "pensione tõsta", "kaitsekulutusi tõsta"},
                 {"lasteaiaõpetajate palku tõsta", "kindlustada tasuta hambaravi kuni 30-aastastele"},
                 {"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},
                 set()])

