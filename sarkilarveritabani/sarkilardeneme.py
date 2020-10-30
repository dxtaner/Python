from sarkilar import *

print("""*********************

Sarkilar Programına Hoşgeldiniz.

İşlemler;

1. Sarkilari Göster
2. Sarki Ekle
3. Sarki Sil 
4. Toplam Sarki Süresini Hesapla 
5. En Yüksek Süreli Sarkiyi Goster
6. Toplam Sarki Sayisini Goster

Çıkmak için 'q' ya basın.
*************************""")

sarkilar = Sarkilar()

while True:
    işlem = input("Yapacağınız İşlem:")

    if (işlem == "q"):
        print("Programdan Cikiliyor...")
        break
    elif (işlem == "1"):
        sarkilar.sarkilarigoster()
    elif (işlem == "2"):
        sarkiismi = input("Sarki İsim:")
        sarkiciadi = input("Sarkici Adi:")
        album = input("Prodiksiyon Sirketi:")
        prodiksiyonsirketi = input("Album:")
        sarkisuresi = int(input("Sarki Süresi:"))

        yenisarki = Sarki(sarkiismi,sarkiciadi,album,prodiksiyonsirketi,sarkisuresi)
        print("Sarki Ekleniyor.")
        time.sleep(2)
        sarkilar.sarkiekle(yenisarki)
        print("Sarki Eklendi..")
    elif (işlem == "3"):
        isim = input("Hangi sarkiyi silmek istiyorsunuz ?")
        print("Sarki Siliniyor...")
        time.sleep(2)
        sarkilar.sarkisil(isim)
        print("Sarki silindi....")
    elif (işlem == "4"):
        print("toplam sure hesaplaniyor..")
        time.sleep(2)
        sarkilar.toplamsarkisuresi()
    elif (işlem == "5"):
        print("en yuksek sureli sarkı aranıyor... ")
        time.sleep(2)
        sarkilar.enyukseksurelisarki()
    elif(işlem=="6"):
        sarkilar.toplamsarkisayisi()
    else:
        print("Geçersiz İşlem...")
