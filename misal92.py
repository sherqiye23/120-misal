#92ci sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Bu siyahıda ilk rast gəlinən mənfi ədədə qədər olan elementlərin artan sıra ilə düzüldüyünü təyin edin. Əgər belədirsə, ekrana  YES, əks halda NO çıxarın.
from random import*
list=[randint(-40,60) for k in range(10)]
print(list)
x=[]
for i in list:
	if i<0:
		x.append(i)
		
a=list.index(x[0])
newList=list[:a]

if len(newList) == 0:
	print(' element yoxdu')
elif len(newList) == 1:
	print(' element azdı')

elif newList == newList.sort():
	print(' YES')
elif newList != newList.sort():
	print(' NO')
