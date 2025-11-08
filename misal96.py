#96cı sual
#Təsadüfi tam ədədlərdən ibarət bir siyahı yaradın. Bu siyahıdan K-cı mövqedən başlayaraq M-sayda element seçib bu elementlərdən ibarət yeni siyahı yaradaraq onu ekrana çıxarın.
from random import*
def yeniList(list,k,n):
	a=list[k:m+1]
	print(a)
	
list=[randint(1,100) for k in range(11)]
print(list)
k= int(input(" k-nı yazın: "))
m= int(input(" m-i yazın: "))
n=m-k

yeniList(list,k,n)