import time
import random

print("XXXXXXX----Sayi Tahmin---XXXXXXX\n")

rastgelesayi=random.randint(1,50)
hakkimiz=5

while True:
    tahminim=int(input("\nsayi tahminin :"))

    if(tahminim==rastgelesayi):
        print(tahminim," = ",rastgelesayi, "tahminiz dogru")
        break
    elif(tahminim<rastgelesayi):
        print("tahmine bakiliyor")
        time.sleep(2)
        hakkimiz-=1
        print("daha yuksek sayi girin ")
    else:
        print("tahmine bakiliyor")
        time.sleep(2)
        hakkimiz-=1
        print("daha dusuk sayi girin")
    if(hakkimiz==0):
        print("tahmin hakki bitti...")
        print("sayimiz",rastgelesayi)
        break

