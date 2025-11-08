#18ci sual
#Bütün üçrəqəmli Armstronq ədədləri tapın.  Məsələn, Armstronq ədədi 153=1³+5³+3³
def armstrong(x):
    y=0
    for i in str(x):
        y+=int(i)**3
        if int(y)==int(x):
            return x
        
for x in range(100,1000):
    if x == armstrong(x):
        print(' ',x)
