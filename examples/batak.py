import random


class BatakOyunu:
    def __init__(self, oyuncu_sayisi):
        self.oyuncu_sayisi = oyuncu_sayisi
        self.oyuncular = ["Oyuncu " + str(i+1) for i in range(oyuncu_sayisi)]
        self.kartlar = self.oyuncu_sayisi * 13
        self.elindeki_kartlar = {oyuncu: [] for oyuncu in self.oyuncular}
        self.masadaki_kartlar = []

    def kart_dagit(self):
        destedeki_kartlar = [i+1 for i in range(self.kartlar)]
        random.shuffle(destedeki_kartlar)

        for oyuncu in self.oyuncular:
            for _ in range(4):
                kart = destedeki_kartlar.pop()
                self.elindeki_kartlar[oyuncu].append(kart)

        self.masadaki_kartlar = [destedeki_kartlar.pop() for _ in range(4)]

    def oyunu_baslat(self):
        self.kart_dagit()

        print("Batak Oyunu Başladı!")
        print("Masadaki Kartlar:", self.masadaki_kartlar)
        print("------------------------")

        for oyuncu in self.oyuncular:
            print(oyuncu, ":", self.elindeki_kartlar[oyuncu])

    def oyunu_oyna(self):
        self.oyunu_baslat()

        for tur in range(13):
            print("------------------------")
            print("Tur", tur+1)

            for oyuncu in self.oyuncular:
                print(oyuncu, "sırası")
                kart = self.elindeki_kartlar[oyuncu].pop(0)
                print("Oynanan Kart:", kart)

                if kart in self.masadaki_kartlar:
                    self.masadaki_kartlar.remove(kart)
                else:
                    self.masadaki_kartlar.append(kart)

                self.elindeki_kartlar[oyuncu].append(
                    self.masadaki_kartlar.pop(0))

                print("Masadaki Kartlar:", self.masadaki_kartlar)
                print(oyuncu, ":", self.elindeki_kartlar[oyuncu])
                print("------------------------")

        print("Oyun Bitti!")
        print("Sonuçlar:")

        for oyuncu in self.oyuncular:
            print(oyuncu, ":", self.elindeki_kartlar[oyuncu])

        print("Masadaki Kartlar:", self.masadaki_kartlar)


oyun = BatakOyunu(4)
oyun.oyunu_oyna()
