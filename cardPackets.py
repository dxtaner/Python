def kartPaketleri(kartTipleri):
    sonuc = len(kartTipleri)
    enBuyukSayi = max(kartTipleri)

    sayac = [0] * (enBuyukSayi + 1)

    # Kart tiplerinin sayısını sayan bir dizi oluşturun
    for i in range(len(kartTipleri)):
        sayac[kartTipleri[i]] += 1

    # Minimum ek kart sayısını hesaplamak için işlem yapın
    for basamak in range(2, enBuyukSayi + 1):
        geciciSonuc = 0
        i = 0
        while i <= enBuyukSayi and geciciSonuc < sonuc:
            # Kart türlerini eşit sayıda paketlemek için ek kart sayısını hesaplayın
            geciciSonuc += sayac[i] * ((basamak - (i % basamak)) % basamak)
            i += 1
        sonuc = min(sonuc, geciciSonuc)

    return sonuc


if __name__ == '__main__':
    kartTipleriSayisi = int(input("Kart türü sayısını girin: "))
    kartTipleri = []

    # Kullanıcıdan kart tiplerinin adedini giriş olarak alın
    for _ in range(kartTipleriSayisi):
        kartTipi = int(input(f"{_+1}. kart türünün adedini girin: "))
        kartTipleri.append(kartTipi)

    # Minimum ek kart sayısını hesaplayın ve sonucu yazdırın
    sonuc = kartPaketleri(kartTipleri)
    print(f"Minimum ek kart sayısı: {sonuc}")
