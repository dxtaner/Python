
a=int(input("sayi girin:"))
b=int(input("sayi girin:"))
c=int(input("sayi girin:"))

delta = b*b -4*a*c
x1=(-b-delta ** 0.5) / (2*a)
x2=(-b+delta ** 0.5) / (2*a)

print("x1:{} \nx2:{}".format(x1,x2))