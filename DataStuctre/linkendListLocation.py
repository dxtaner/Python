class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None


class BagliListe:
    def __init__(self):
        self.baslangic = None

    def ekle(self, veri):
        yeni_dugum = Node(veri)
        if self.baslangic is None:
            self.baslangic = yeni_dugum
        else:
            son_dugum = self.baslangic
            while son_dugum.sonraki:
                son_dugum = son_dugum.sonraki
            son_dugum.sonraki = yeni_dugum

    def eleman_konumu(self, hedef_veri):
        simdiki_dugum = self.baslangic
        konum = 0

        while simdiki_dugum:
            if simdiki_dugum.veri == hedef_veri:
                return konum
            konum += 1
            simdiki_dugum = simdiki_dugum.sonraki

        return -1  # Hedef veri bulunamazsa -1 döndürülür

    def listeyi_goster(self):
        dugum = self.baslangic
        while dugum:
            print(dugum.veri, end=" -> ")
            dugum = dugum.sonraki
        print("None")


# Bağlı liste oluşturma ve kullanma
liste = BagliListe()
liste.ekle(10)
liste.ekle(20)
liste.ekle(30)

print("Bağlı Liste:")
liste.listeyi_goster()

hedef = 20
konum = liste.eleman_konumu(hedef)

if konum != -1:
    print(f"{hedef} elemanı {konum}. pozisyonda bulundu.")
else:
    print(f"{hedef} elemanı bulunamadı.")
