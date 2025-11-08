#21ci sual
#k-rəqəmli Armstronq ədədləri tapın (2<k<10)
def armstrong(x):
    y=0
    for i in str(x):
        y+=int(i)**3
        if int(y)==int(x):
            return x
        
for x in range(100, 1000000000):
    if x == armstrong(x):
        print(" ",x)