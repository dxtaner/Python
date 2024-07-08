import webbrowser as wb
import time
import sqlite3 as sql
from InstagramAPI import InstagramAPI
import tweepy


# Veritabanı Bağlantısı
def veritabani_baglan():
    return sql.connect('tv.sqlite')


# Tablo Oluşturma
def tablo_olustur(vt):
    imlec = vt.cursor()
    imlec.execute(
        "CREATE TABLE IF NOT EXISTS program(TVad,Tvadres,Radyoad,Radyoadres,fbid,fbpas,instaid,instapas,twid,twpas)")
    vt.commit()


# TV Fonksiyonu
def TV():
    while True:
        kanal_sec = int(input(
            "Bir Kanal seçiniz...\n[1] TRT\n[2] SHOW\n[3] KANAL D\n[4] STAR\n[5] HABERTÜRK\n[6] TLC\n[7] CNN\n[8] NTV\n[9]Geri"))
        if 1 <= kanal_sec <= 8:
            wb.open_new(
                f"https://www.youtube.com/watch?v=DVOgoBnGAs0{['', '?v=KSe7H96-rS8', '?v=VlNIxWdT_Yw', '?v=qWmZKP2TzGc', '?v=rtTDYzG9vXM', '?v=s-KKgm4ysjk', '?v=IMy6RvwMJLs', '?v=I6ISnq4qyY0', '?v=XEJM4Hcgd3M'][kanal_sec - 1]}")
        elif kanal_sec == 9:
            return
        else:
            print("HATALI İŞLEM")


# Twitter Fonksiyonu
def Twitter():


# [Önceki kod devam ediyor...]

# Instagram Fonksiyonu
def Instagramm(username, password):


# [Önceki kod devam ediyor...]

# Interaktif Fonksiyonu
def Interaktif():


# [Önceki kod devam ediyor...]

# Radyo Fonksiyonu
def Radyo():
    while True:
        kanallar = ["Fenomen", "JoyTürk", "PowerTürk", "45likler"]
        adresler = ["https://www.youtube.com/watch?v=KSe7H96-rS8", "https://www.youtube.com/watch?v=VlNIxWdT_Yw",
                    "https://www.youtube.com/watch?v=qWmZKP2TzGc", "https://www.youtube.com/watch?v=rtTDYzG9vXM"]

        for idx, kanal in enumerate(kanallar, start=1):
            print(f"[{idx}] {kanal}")
        print("[9] Geri\n[10] Radyo Kanalı Ekle")

        secim = int(input("Uygulama Seçiniz: "))
        if 1 <= secim <= len(kanallar):
            wb.open_new(adresler[secim - 1])
        elif secim == 9:
            return
        elif secim == 10:
            kanalismi = input("Eklemek istediğiniz kanal ismi:")
            kanal = input("Kanal Adresi:")
            kanallar.append(kanalismi)
            adresler.append(kanal)
        else:
            print("HATALI İŞLEM")


# Ana Döngü
def main_loop():
    while True:
        print("----------- TV ------------\n")
        secimy = int(input("Merhaba bir işlem seçin\n\t1-TV 2-Radyo 3-İnteraktif 4-Kapat"))

        if secimy == 1:
            TV()
            print("---------------------------")
        elif secimy == 2:
            Radyo()
            print("---------------------------")
        elif secimy == 3:
            Interaktif()
            print("---------------------------")
        elif secimy == 4:
            print("Sistem Kapatlıyor..")
            time.sleep(2)
            print(" : Hoşçakal : ")
            break
        else:
            print("HATALI İŞLEM YAPILDI\n")


if __name__ == "__main__":
    veritabani = veritabani_baglan()
    tablo_olustur(veritabani)
    main_loop()
