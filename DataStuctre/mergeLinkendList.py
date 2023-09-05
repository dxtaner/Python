class Node:
    def __init__(self, veri):
        self.veri = veri
        self.sonraki = None


def merge(liste1, liste2):
    yeni_baslangic = Node(None)  # Geçici bir başlangıç düğümü oluşturun
    current = yeni_baslangic  # Gezgin düğümü başlangıç düğümü olarak ayarlayın

    while liste1 is not None and liste2 is not None:
        if liste1.veri < liste2.veri:
            current.sonraki = liste1
            liste1 = liste1.sonraki
        else:
            current.sonraki = liste2
            liste2 = liste2.sonraki
        current = current.sonraki

    # İlk bağlı listenin veya ikinci bağlı listenin sonuna geldiğimizde,
    # geriye kalan düğümleri ekleyin
    if liste1 is not None:
        current.sonraki = liste1
    elif liste2 is not None:
        current.sonraki = liste2

    # Geçici başlangıç düğümünü atlayarak birleştirilmiş bağlı listeyi döndürün
    return yeni_baslangic.sonraki

# Yardımcı fonksiyon: Bağlı listeyi yazdırmak için


def listeyi_goster(baslangic):
    current = baslangic
    while current:
        print(current.veri, end=" -> ")
        current = current.sonraki
    print("None")


# İlk bağlı liste oluşturma
liste1 = Node(10)
liste1.sonraki = Node(20)
liste1.sonraki.sonraki = Node(30)

# İkinci bağlı liste oluşturma
liste2 = Node(15)
liste2.sonraki = Node(25)
liste2.sonraki.sonraki = Node(35)

print("İlk Bağlı Liste:")
listeyi_goster(liste1)

print("İkinci Bağlı Liste:")
listeyi_goster(liste2)

birlesmis_liste = merge(liste1, liste2)

print("Birleştirilmiş Bağlı Liste:")
listeyi_goster(birlesmis_liste)
