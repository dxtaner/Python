class calisan():
    def __init__(self,ad,maas,depertman):
        self.ad=ad
        self.maas=maas
        self.depertman=depertman

    def bilgilerigoster(self):
        print("calisan bilgileri")
        print("ad :{}\nmaas :{}\ndepertman :{} ".format(self.ad,self.maas,self.depertman))
    def depertmandegistir(self,yenidepertman):
        self.depertman=yenidepertman

class yonetici(calisan):
    def __init__(self, ad, maas, depertman,kisisayisi):
        super().__init__(ad,maas,depertman)
        self.kisisayisi = kisisayisi
    def bilgilerigoster(self):
        print("yonetici bilgileri")
        print("ad :{}\nmaas :{}\ndepertman :{}\nsorumlu kisi sayisi :{} ".format(self.ad,self.maas,self.depertman,self.kisisayisi))
    def zamyap(self,yenizam):
        self.maas+=yenizam

calisan = calisan("hss",4505,"takım")
calisan.bilgilerigoster()
yonetici = yonetici("taner",3500,"yazilimci",10)
yonetici.bilgilerigoster()
yonetici.depertmandegistir("guvenlik")
yonetici.zamyap(500)
yonetici.bilgilerigoster()
