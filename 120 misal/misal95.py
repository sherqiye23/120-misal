#95ci sual
#Təsadüfi tam ədədlərdən ibarət bir siyahı yaradın. Bu siyahıdan K-cı mövqedən başlayaraq M-sayda elementi silin.
from random import*
def clear(list,k,n):
	del list[k:m+1]
	print(list)
	
list=[randint(1,100) for k in range(11)]
print(list)
k= int(input(" k-nı yazın: "))
m= int(input(" m-i yazın: "))
n=m-k

clear(list,k,n)