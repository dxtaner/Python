import datetime

def hafta_numarasi_bul(tarih_str):
    # Kullanıcıdan alınan tarih stringini datetime nesnesine çeviriyoruz
    tarih = datetime.datetime.strptime(tarih_str, "%Y-%m-%d")
    hafta_numarasi = tarih.strftime("%U")  # Hafta numarasını alıyoruz
    return int(hafta_numarasi)


# Kullanıcıdan tarih bilgisini alalım
kullanici_tarihi = input("Tarih (YYYY-AA-GG formatında) giriniz: ")
hafta_numarasi = hafta_numarasi_bul(kullanici_tarihi)
print(f"Girilen tarihin bulunduğu yıldaki hafta numarası: {hafta_numarasi}")
