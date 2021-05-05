try:
    a=int(input("bir sayi girin:"))
    b=int(input("bir sayi girin:"))
    print(a/b)
except ValueError:
    print("inputu dogru girin\nhata olustu")
except ZeroDivisionError:
    print("sifira bolunme hatasi")
finally:
    print("finally blogu ")
print("hata bloklarından cıkıldı")