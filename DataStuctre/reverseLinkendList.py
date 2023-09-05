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

    def ters_cevir(self):
        onceki_dugum = None
        simdiki_dugum = self.baslangic
        sonraki_dugum = None

        while simdiki_dugum is not None:
            sonraki_dugum = simdiki_dugum.sonraki
            simdiki_dugum.sonraki = onceki_dugum
            onceki_dugum = simdiki_dugum
            simdiki_dugum = sonraki_dugum

        self.baslangic = onceki_dugum

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

liste.ters_cevir()

print("Bağlı Liste (Ters Çevrilmiş):")
liste.listeyi_goster()
