def kokbulma(a,b,c):
    delta=(b*b-4*a*c)
    if delta<0:
        print("real kok yoktur")
        return
    else:
        x1= (-b -delta**0.5)/2*a
        x2= (-b +delta**0.5)/2*a
        return (x1,x2)

a= int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

sonuc=kokbulma(a,b,c)
print(sonuc)