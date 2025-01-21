print("-----------------Hesap Makinasi------------------")
print("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme")
print("--------------------------------")

a = int(input("Bir sayi giriniz :"))
b = int(input("Bir sayi giriniz :"))

islem = int(input("islem seciniz :"))

if islem==1:
    print("Toplam:",a+b)
elif islem==2:
    print("Çıkarma:",a-b)
elif islem==3:
    print("Çarpma:",a*b)
elif islem==4:
    print("Bölme:",a//b)
else:
    print("Gecersiz İslem")

