#93cü sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Bu siyahıda ilk rast gəlinən mənfi ədədə qədər olan elementlərin azalan sıra ilə düzüldüyünü təyin edin. Əgər belədirsə, ekrana  YES, əks halda NO çıxarın.
from random import*
list=[randint(-40,60) for k in range(10)]
print(list)
x=[]
for i in list:
	if i<0:
		x.append(i)

a=list.index(x[0])
newList=list[:a]
c = newList.copy()
newList.sort()
newList.reverse()

if len(newList) == 0:
	print(' element yoxdu')
elif len(newList) == 1:
	print(' element azdı')
	
elif c == newList:
	print(' YES')
else:
	print(' NO')