import  random
import  time

class kumanda():
    def __init__(self,tv_durum="Kapali",tv_ses=0,kanal_listesi = ["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tvac(self):

        if(self.tv_durum=="Açık"):
            print("Tv zaten acik..")
        else:
            print("Tv aciliyorr....")
            self.tv_durum="Açık"

    def tvkapat(self):

         if (self.tv_durum == "Kapali"):
             print("Tv zaten kapali..")
         else:
             print("Tv kapatiliyor....")
             self.tv_durum = "Kapali"

    def sesayarlari(self):

          while True:
              islem=input("Sesi azalt : < \nSesi yukselt : > \ncikis icin tusa basin ")

              if islem=="<":
                  if self.tv_ses !=0:
                      self.tv_ses-=1
                      print("ses:",self.tv_ses)
              elif islem==">":
                  if self.tv_ses <= 30:
                      self.tv_ses+=1
                      print("ses:",self.tv_ses)
              else:
                  print("yeni ses :",self.tv_ses)
                  break

    def kanalekleme(self):
            kan=input("kanal ismi girin :")
            print("kanal ekleniyor...")
            time.sleep(2)
            self.kanal_listesi.append(kan)
            print("kanal eklendi")

    def rastgelekanal(self):
            rast=random.randint(0,len(self.kanal_listesi)-1)
            self.kanal=self.kanal_listesi[rast]

            print("suanki kanal: ",self.kanal)

    def __len__(self):
          return len(self.kanal_listesi)

    def __str__(self):
          return "tv durumu : {} \ntv ses : {} \nkanallistesi : {} \nsuanki kanal : {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda= kumanda()

print("""
Televizyon Uygulaması

1. Televizyonu Aç

2. Televizyonu Kapat

3. Televizyon Bilgileri

4. Kanal Sayısını Öğrenme

5. Kanal Ekle

6. Rastgele Kanal'a Geç

7. Sesi Azalt Ya da Artır

Çıkmak için 'q' ya basın.
*******************""")

while True:

    islem=input("islemi secin:")

    if(islem=="q"):
        print("uygulamadan cikiliyor...")
        break
    elif (islem=="1"):
        kumanda.tvac()
    elif (islem == "2"):
         kumanda.tvkapat()
    elif (islem == "3"):
        print(kumanda)
    elif (islem == "4"):
       print("kanal sayisi :",len(kumanda))
    elif (islem == "5"):
        kumanda.kanalekleme()
    elif (islem == "6"):
        kumanda.rastgelekanal()
    elif (islem == "7"):
        kumanda.sesayarlari()
    else:
        print("gecersiz islem")

