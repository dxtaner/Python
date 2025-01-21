ad = ["Arda","Tarık","Ezgi","Kemal","Ali","Selim","Merve","Cevdet"]
soyad = ["Yılmaz","Ozkan","Samsun","Kaya","Yılmaz","Kaya","Ercan","Yıldırım"]

liste=list(zip(ad, soyad))
liste.sort()

print("Eşleştirme")
print("*************")
for i,j in liste:
    print(i , j)

