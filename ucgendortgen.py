deger = input("Ucgen mi? Dortgen mi? :\n")

if deger=="ucgen":
    print("Kenarlari girin :")
    a = int(input("kenar:"))
    b = int(input("kenar:"))
    c = int(input("kenar:"))
    if a==b and b==c:
        print("Eskenar ucgen")
    elif a==b and b!=c:
        print("Ikizkenar ucgen")
    elif a!=b and b!=c:
        print("Cesitkenar ucgen")
    else:
        print("Ucgen degil")
elif deger=="dortgen":
    a = int(input("kenar:"))
    b = int(input("kenar:"))
    c = int(input("kenar:"))
    d = int(input("kenar:"))
    if a == b and b == c and c == d:
        print("Kare")
    elif (a==c and b==d):
        print("Dikdortgen")
    else:
        print("Diger dortgenler")
else:
    print("Yanlıs Deger Girisi")