def ebob(sayi1,sayi2):
    ebob=1
    i=2
    while i<sayi2:
        if(sayi1%i==0 and sayi2%i==0):
            ebob=i
        i+=1
    return ebob


while True:
    a=int(input("sayi girin :"))
    b=int(input("sayi girin :"))

    if a>=b:
        e=ebob(b,a)
        break
    else:
        e=ebob(a,b)
        break

print(e)