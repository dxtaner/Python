with open("futbolcular.txt","r",encoding= "utf-8") as file:

    fb=[]
    gs=[]
    bjk=[]

    for satir in file:

        satir = satir[:-1]
        liste = satir.split(",")
        isim = liste[0]
        takim = liste[1]

        if (takim == "Fenerbahçe"):
            fb.append(isim + "--->" + takim+"\n")
        elif (takim == "Galatasaray"):
            gs.append(isim + "--->" + takim+"\n")
        elif (takim == "Beşiktaş"):
            bjk.append(isim + "--->" + takim+"\n")

with open("fb.txt", "w", encoding="utf-8") as file2:
    for i in fb:
        file2.write(i)
with open("gs.txt", "w", encoding="utf-8") as file3:
    for i in gs:
        file3.write(i)
with open("bjk.txt", "w", encoding="utf-8") as file4:
    for i in bjk:
        file4.write(i)