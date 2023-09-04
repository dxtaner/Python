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

    def eleman_sil(self, hedef_veri):
        simdiki_dugum = self.baslangic
        onceki_dugum = None

        while simdiki_dugum:
            if simdiki_dugum.veri == hedef_veri:
                if onceki_dugum:
                    onceki_dugum.sonraki = simdiki_dugum.sonraki
                else:
                    self.baslangic = simdiki_dugum.sonraki
                return

            onceki_dugum = simdiki_dugum
            simdiki_dugum = simdiki_dugum.sonraki

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

# Eleman silme
liste.eleman_sil(20)
print("20 elemanı silindikten sonra:")
liste.listeyi_goster()
