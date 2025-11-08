#94cü sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Hər bir mənfi elementdən sonra bu elementin kvadratını siyahıya əlavə edin
from random import*
list=[randint(-50,50) for k in range(5)]
print(list)
i=0
while i<len(list):
	if list[i]<0:
		list.insert(i+1, list[i]**2)
	i+=1
print(list)