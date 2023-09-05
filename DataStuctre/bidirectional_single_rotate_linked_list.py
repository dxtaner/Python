class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None
        self.onceki = None  # Çift yönlü bağlı liste için "onceki" düğümü


def cift_yonlu_to_tek_yonlu(cift_yonlu_baslangic):
    tek_yonlu_baslangic = None
    current = cift_yonlu_baslangic

    while current:
        yeni_dugum = Node(current.veri)
        if not tek_yonlu_baslangic:
            tek_yonlu_baslangic = yeni_dugum
            son_dugum = yeni_dugum
        else:
            son_dugum.sonraki = yeni_dugum
            son_dugum = yeni_dugum
        current = current.sonraki

    return tek_yonlu_baslangic

# Yardımcı fonksiyon: Tek yönlü bağlı listeyi yazdırmak için


def listeyi_goster(baslangic):
    current = baslangic
    while current:
        print(current.veri, end=" -> ")
        current = current.sonraki
    print("None")


# Çift yönlü bağlı liste oluşturma
ilk_cift = Node(1)
ikinci_cift = Node(2)
ucuncu_cift = Node(3)

ilk_cift.sonraki = ikinci_cift
ikinci_cift.onceki = ilk_cift
ikinci_cift.sonraki = ucuncu_cift
ucuncu_cift.onceki = ikinci_cift

print("Çift Yönlü Bağlı Liste:")
listeyi_goster(ilk_cift)

# Dönüşümü uygulama
tek_yonlu_baslangic = cift_yonlu_to_tek_yonlu(ilk_cift)

print("Tek Yönlü Bağlı Liste:")
listeyi_goster(tek_yonlu_baslangic)
