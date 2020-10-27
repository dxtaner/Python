class ikininkuvvetleri():
    def __init__(self,maks):
        self.maks=maks
        self.sayi=1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.sayi<=self.maks):
            sonuc=2**self.sayi
            self.sayi+=1
            return sonuc
        else:
            self.sayi=1
            raise StopIteration

kuvvet=ikininkuvvetleri(6)
iterator = iter(kuvvet)

for i in kuvvet:
    print(i)
