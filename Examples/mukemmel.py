sayi=int(input("bir sayi girin :"))
toplam=0
i=1
while i<sayi:
    if(sayi % i == 0):
        toplam+=i
    i+=1
if(toplam==sayi):
    print(sayi," sayisi mukemmel sayidir")
else:
    print(sayi," sayisi mukemmel sayi degildir")
