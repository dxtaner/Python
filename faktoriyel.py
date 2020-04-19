faktoriyel =1

while(True):
    sayi = int(input("Sayi Girin :"))
    faktoriyel =1
    if sayi<=0:
        print("pozitif sayı girin ")
    else:
        for i in range(1,sayi+1):
            faktoriyel*=i
        print("Faktoriyel :",faktoriyel)
        break