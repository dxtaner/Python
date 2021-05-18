class yazilimci():

    def __init__(self,isim,soyad,maas,yas,diller):
        self.isim=isim
        self.soyad=soyad
        self.maas=maas
        self.yas=yas
        self.diller=diller

    def bilgilerigoster(self):
        print("""
        yazilimcinin bilgileri 
        isim : {}
        soyad : {}
        maas : {}
        yas : {}
        bildigi diller : {}
        
        """.format(self.isim,self.soyad,self.maas,self.yas,self.diller))

    def zamyap(self):
        zam=int(input("zam miktarini girin :"))
        print("zam yapiliyor....")
        self.maas+=zam

    def dilekle(self):
        dil=input("ekleyeceginiz dili girin :")
        print("dil ekleniyor...")
        self.diller.append(dil)

yazilimci1 = yazilimci("taner","özer",4500,26,["java","c","python"])

while True:
    print("""
        ****************
        1- yazilimcinin bilgilerini göster
        2- yazilimciya dil ekle    
        3- yazilimciya zam yap
        cikis icin q'ya basin
        **************
    """)
    secim=input("secim yapin :")
    if(secim=='q'):
        print("cikis yapiliyor")
        break
    elif (int(secim)==1):
        yazilimci1.bilgilerigoster()
    elif (int(secim)==2):
        yazilimci1.dilekle()
    elif (int(secim)==3):
         yazilimci1.zamyap()
    else:
        print("gecersiz secim")


