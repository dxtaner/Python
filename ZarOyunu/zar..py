import time
import random

print("************ZAR OYUNUNA HOŞGELDİNİZ******-*****")

# Kullanıcıdan kaç deneme hakkı istediğini alalım
tahmin = int(input("Kaç deneme sonra tüm zarların üst yüzü 6 olur? "))

deneme = 0
while deneme < tahmin:
    zar1 = random.randint(1, 6)  # Rastgele bir zar değeri seçelim
    zar2 = random.randint(1, 6)  # Rastgele bir zar değeri seçelim

    print("\nİlk zar:", zar1)
    print("İkinci zar:", zar2)

    if zar1 == zar2 == 6:
        print("\nTEBRİKLER!")
        print("Zarların üst yüzü 6 sayısını göstermektedir.")
        print("Oyunu kazandınız!")
        break
    else:
        print("\nZarlar 6 sayısını göstermiyor...")
        time.sleep(1)
        deneme += 1

if deneme == tahmin:
    print("\nHakkınız doldu.")
    print("Oyunu kazanamadınız.")
