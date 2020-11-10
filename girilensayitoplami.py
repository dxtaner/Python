toplam=0

while True:
    sayi = input("sayi girin (cikmak icin q ya basin) :")
    if(sayi=="q"):
        print("cikis yapiliyor")
        break
    toplam += int(sayi)
print("toplam sayi :", toplam)