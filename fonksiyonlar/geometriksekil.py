def geo(sekil):
    if len(sekil)==3:
        a=sekil[0]
        b=sekil[1]
        c=sekil[2]
        if a+b>c and a+c>b and b+c>a:
            if a==b and a==c and b==c:
                print("eşkenar üçgen")
            elif a==b and a==c:
                print("ikizkenar üçgen")
            else:
                print("çeşitkenar üçgen")
        else:
            print("ucegen belirtmiyor")

    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]
        if a==b and a==c and a==d:
            print("kare")
        elif a==c and b==d:
            print("dikdörtgen")
        else:
            print("normal dörtgen")
    else:
        print("herhangi bir sekil değil")



while True:
    elemansayisi = int(input("eleman sayisi girin :"))
    if elemansayisi==3:
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geo([a,b,c])
    elif elemansayisi==4:
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geo([a,b,c,d])
    else:
        print("tekrar girin..")
