import  sqlite3
import time

class Sarki():

    def __init__(self,sarkiismi,sarkiciadi,album,prodiksiyonsirketi,sarkisuresi):

        self.sarkiismi=sarkiismi
        self.sarkiciadi=sarkiciadi
        self.album=album
        self.prodiksiyonsirketi=prodiksiyonsirketi
        self.sarkisuresi=sarkisuresi

    def __str__(self):
        return "Sarki İsmi: {}\nSanatci: {}\nAlbum: {}\nProdiksiyon Sirketi: {}\nSarki Suresi: {}\n".\
            format(self.sarkiismi,self.sarkiciadi,self.album,self.prodiksiyonsirketi,self.sarkisuresi)

class Sarkilar():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("sarkilar.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists sarkilar (sarkiismi TEXT,sarkiciadi TEXT,album TEXT,prodiksiyonsirketi TEXT,sarkisuresi INT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def sarkilarigoster(self):

        sorgu =  "Select * From sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        if (len(sarkilar) == 0):
            print("Listede sarki bulunmuyor...")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarkiekle(self,sarki):
        sorgu = "Insert into sarkilar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.sarkiismi,sarki.sarkiciadi,sarki.album,sarki.prodiksiyonsirketi,sarki.sarkisuresi))
        self.baglanti.commit()

    def sarkisil(self,sarkiismi):
        sorgu = "Delete From sarkilar where sarkiismi = ?"
        self.cursor.execute(sorgu,(sarkiismi,))
        self.baglanti.commit()

    def toplamsarkisuresi(self):
         sorgu = "Select * From sarkilar "
         self.cursor.execute(sorgu)
         sarkilar = self.cursor.fetchall()
         toplamsure=0
         for i in sarkilar:
             sarki=Sarki(i[0],i[1],i[2],i[3],i[4])
             toplamsure+=(sarki.sarkisuresi)
         print("toplam sarkı süresi :",toplamsure)

    def enyukseksurelisarki(self):
        sorgu="Select * From sarkilar"
        self.cursor.execute(sorgu)
        sarkilar=self.cursor.fetchall()
        yukseksurelisarki=0
        index=Sarki([0],[1],[2],[3],[4])
        for i in sarkilar:
            sarki = Sarki(i[0], i[1], i[2], i[3], i[4])
            if(sarki.sarkisuresi>yukseksurelisarki):
               yukseksurelisarki=sarki.sarkisuresi
               index=i
        print("en yüksek süreli sarki:")
        for j in index:
            print(j)

    def toplamsarkisayisi(self):
        sorgu = "Select * From sarkilar"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()

        print("listedeki toplam sarki sayisi:",len(sarkilar))
