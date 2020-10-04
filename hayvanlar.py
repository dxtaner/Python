class hayvan():
    def __init__(self,ad,tur,cinsiyet,yas,dissayisi,ayaksayisi):
        self.ad=ad
        self.tur=tur
        self.cinsiyet=cinsiyet
        self.yas=yas
        self.dissayisi=dissayisi
        self.ayaksayisi=ayaksayisi

    def bilgilerigoster(self):
        print("""
        hayvanın bilgileri 
        isim : {}
        turu : {}
        cinsiyeti : {}
        yas : {}
        dissayisi : {}
        ayaksayisi : {}
        
        """.format(self.ad, self.tur, self.cinsiyet, self.yas, self.dissayisi,self.ayaksayisi))

    def yasarttir(self,artiyas):
        self.yas+=artiyas
        print("hayvanın yasi artirildi yeni yas :",self.yas)

class kopek(hayvan):
    def __init__(self,ad,tur,cinsiyet,yas,dissayisi,ayaksayisi,azidisi):
        super().__init__(ad,tur,cinsiyet,yas,dissayisi,ayaksayisi)
        self.azidisi=azidisi

    def disarrtir(self,sayi):
        self.azidisi+=sayi
        print("azi disi sayisi artti ")

    def bilgilerigoster(self):
        print("kopek bilgileri")
        print("ad :{}\ntur :{}\ncinsiyet :{}\nyas :{}\ndissayisi : {}\nayaksayisi : {}\nazidisi sayiisi : {} ".format(self.ad, self.tur, self.cinsiyet,
                                                                                 self.yas,self.dissayisi,self.ayaksayisi,self.azidisi))

class kus(hayvan):
    def __init__(self, ad, tur, cinsiyet, yas, dissayisi, ayaksayisi,kanatsayisi):
        super().__init__(ad, tur, cinsiyet, yas, dissayisi, ayaksayisi)
        self.kanatsayisi=kanatsayisi

    def kanatcirp(self,sayi):
        print("kusumuz",sayi,"kadar kanat cirpiyor")

    def bilgilerigoster(self):
        print("kus bilgileri")
        print("ad :{}\ntur :{}\ncinsiyet :{}\nyas :{}\ndissayisi : {}\nayaksayisi : {}\nkanatsayisi : {} ".format(self.ad, self.tur, self.cinsiyet,
                                                                                 self.yas,self.dissayisi,self.ayaksayisi,self.kanatsayisi))

class at(hayvan):
    def __init__(self, ad, tur, cinsiyet, yas, dissayisi, ayaksayisi,kuyrukuzunlugu):
        super().__init__(ad, tur, cinsiyet, yas, dissayisi, ayaksayisi)
        self.kuyrukuzunlugu=kuyrukuzunlugu

    def kos(self,sayi):
        print("at",sayi," m kadar kosuyor")

    def bilgilerigoster(self):
        print("at bilgileri")
        print("ad :{}\ntur :{}\ncinsiyet :{}\nyas :{}\ndissayisi : {}\nayaksayisi : {}\nkuyruk uzunlugu : {} ".format(self.ad, self.tur, self.cinsiyet,
                                                                                 self.yas,self.dissayisi,self.ayaksayisi,self.kuyrukuzunlugu))



kus = kus("sadık","kus","disi",2,10,4,6)
kus.bilgilerigoster()

hayvan = hayvan("umar","at","erkek",12,12,4)
hayvan.yasarttir(4)
hayvan.bilgilerigoster()

kopek = kopek("comar","it","disi",5,32,4,5)
kopek.bilgilerigoster()

at = at("semir","at","erkek",5,15,4,1)
at.yasarttir(2)
at.kos(200)
at.bilgilerigoster()