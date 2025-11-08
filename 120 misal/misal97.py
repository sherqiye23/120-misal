#97ci sual
#Təsadüfi tam ədədlərdən ibarət bir siyahı yaradın. Bu siyahının elementləri cəmini və müsbət elementlırinin sayını siyahıda 1-ci və 2-ci mövqeyə əlavə edin
from random import*
def toplama(list):
	sum=1
	for i in list:
		sum+=i
	return sum


list=[randint(-50,50) for k in range(10)]
print(list)

a = toplama(list)
print(f" Elementlər cəmi: {a}")
x=[]
for k in list:
	if k>0:
		x.append(k)

b = len(x)
print(f" Müsbət elementlərinin sayı: {b}")

list.insert(1,a)
list.insert(2,b)
print(list)
