sayi=(input("bir sayi girin :"))
basamak= len(sayi)
sayi=int(sayi)
bas=0
toplam=0
gsayi=sayi
while gsayi>0:
     bas=gsayi%10
     toplam+=bas**basamak
     gsayi//=10

if (toplam == sayi):
    print(sayi, "bir armstrong sayısıdır.")
else:
    print(sayi, "bir armstrong sayısı değildir.")