import sqlite3 as sql
import time

vt = sql.connect('program.sqlite')
imlec = vt.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS program(ders_adi TEXT, ders_gunu INTEGER, ders_saati TEXT, ders_yeri TEXT)")

print("----------------- DERS PROGRAMIM -----------------")


def ders_ekle():
    ders_adi = input("Eklenecek dersin ismini veya kodunu giriniz: ")
    ders_gunu = int(input("1-Pazartesi, 2-Salı, 3-Çarşamba, 4-Perşembe, 5-Cuma, 6-Cumartesi, 7-Pazar: "))
    ders_saati = input("Ders saatinizi giriniz: ")
    ders_yeri = input("Dersin yapılcağı dersliği giriniz: ")

    imlec.execute('INSERT INTO program (ders_adi, ders_gunu, ders_saati, ders_yeri) VALUES (?, ?, ?, ?)',
                  (ders_adi, ders_gunu, ders_saati, ders_yeri))
    vt.commit()
    print(f"{ders_adi} dersi programınıza eklendi.")


def ders_cikar():
    ders_adi = input("Çıkarılacak dersin ismini veya kodunu giriniz: ")
    imlec.execute("DELETE FROM program WHERE ders_adi = ?", (ders_adi,))
    vt.commit()
    print(f"{ders_adi} dersi programınızdan çıkarıldı.")


def ders_guncelle():
    gun_secenek = int(input("[1]Ders Adı, [2]Ders Günü, [3]Ders Saati, [4]Ders Yeri: "))

    ders_adi = input("Güncellenecek dersin ismini veya kodunu giriniz: ")
    yeni_veri = input(f"{ders_adi} için yeni veriyi giriniz: ")

    kolon_isimleri = ["ders_adi", "ders_gunu", "ders_saati", "ders_yeri"]
    imlec.execute(f"UPDATE program SET {kolon_isimleri[gun_secenek - 1]} = ? WHERE ders_adi = ?", (yeni_veri, ders_adi))
    vt.commit()
    print(f"{ders_adi} dersinin bilgisi güncellendi.")


def goster():
    oku = imlec.execute('SELECT ders_adi, ders_gunu, ders_saati, ders_yeri FROM program')
    for ders in oku.fetchall():
        print('Ders İsmi:', ders[0], '--- Ders Günü:', ders[1], '--- Ders Saati:', ders[2], '--- Derslik:', ders[3])
    print("\n\n")


while True:
    secim = input(
        "Programa yapılacak işlemi seçiniz:\n[1] Ders Ekleme, [2] Ders Güncelleme, [3] Ders Çıkarma, [4] Programı Göster\n[Çıkmak için q tuşuna basınız]: ")

    if secim == 'q':
        print("Sistemden çıkılıyor...")
        time.sleep(2)
        print("Sistemden başarıyla çıkış yapıldı.")
        break
    elif secim == '1':
        ders_ekle()
    elif secim == '2':
        ders_guncelle()
    elif secim == '3':
        ders_cikar()
    elif secim == '4':
        goster()
    else:
        print("Hatalı bir seçim yaptınız.")
        vt.close()
