def ciftmi(sayi):

    if(sayi % 2 ==0):
        return sayi
    else:
        raise ValueError

list=[2,4,5,3,45,41,0,5,56,1,11,12]

for i in list:
    try:
        print(ciftmi(i))
    except ValueError:
        pass