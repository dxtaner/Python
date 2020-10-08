print("islemler\n"
      "1. bakiye sorgula\n"
      "2. para yatirma\n"
      "3. para cekme \n"
      "4. kredi ekleme\n"
      "cikmak icin c'ye basin\n")

bakiye=500

while True:
    islem=input("islem secin :")
    if(islem=="c"):
        print("cikis yapiliyor")
        break
    elif(islem=="1"):
        print("bakiyeniz :",bakiye,"tldir")
    elif(islem=="2"):
        ekle=int(input("eklenecek parayi girin :"))
        bakiye+=ekle
        print("yeni bakiyeniz",bakiye)
    elif(islem=="3"):
        cikar=int(input("cekmek istediginiz parayi girin :"))
        if (cikar>bakiye):
            print("boyle bir parayi cekemezsiniz")
            continue
        else:
            bakiye-=cikar
            print("yeni bakiyeniz", bakiye)
    elif (islem == "4"):
        kredi = int(input('kredi miktarı giriniz:'))
        print('krediniz onaylandı...')
        bakiye += kredi
        print("yeni bakiyeniz", bakiye)
    else:
        print("gecersiz islem")
