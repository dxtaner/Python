def faktoriyel(sayi):
    faktor=1
    for i in range(1,sayi+1):
        faktor*=i
    return faktor

sayi =int(input("bir sayi girin:"))
a=faktoriyel(sayi)
print(a)
