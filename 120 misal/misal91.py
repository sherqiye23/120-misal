#91ci sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Bu siyahı əsasında iki siyahı yaradın. Birinci siyahı müsbət elementlərin kvadratlarından, ikinci siyahı isə isə mənfi elementlərn kublarından ibarət olsun.Alınan yeni siyahıları ekrana çıxarın.
from random import*
list=[randint(-50,50) for k in range(10)]
print(list)
musbet=[]
menfi=[]

for a in list:
	if a>0:
		musbet.append(a)
	if a<0:
		menfi.append(a)	

birinciList=[k**2 for k in musbet]
ikinciList=[k**3 for k in menfi]

print(f' Yeni listlər: {birinciList} və {ikinciList}')