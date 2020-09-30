def asalmi(sayi):
        for j in range(2,sayi):
            if(sayi%j==0):
                return False

        return True

while True:
    sayi=int(input("bir sayi girin:"))
    if(sayi==0):
        print("cikis yapiliyor")
        break
    elif (sayi==1):
        print("asal değildir")
    elif (sayi==2):
        print("sayi asaldir")
    else:
         if (asalmi(sayi)):
            print("sayi asal sayidir")
         else:
            print("asal sayi degildir")
