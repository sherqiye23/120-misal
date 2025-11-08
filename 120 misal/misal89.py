#89cu sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Siyahıya elə bir ədəd daxil edin ki, müsbət ədədlərin cəmi mənfi ədədlərin cəminin moduluna bərabər olsun.

from random import*
def toplama(list):
	sum=0
	for i in list:
		sum+=i
	return sum
	
list=[randint(-50,50) for k in range(10)]
print(list)
musbet=[]
menfi=[]

for a in list:
	if a>0:
		musbet.append(a)
	if a<0:
		menfi.append(a)
	
p=toplama(musbet)
q=toplama(menfi)
print(f' Əvvəlki cəmlər: {p} və {q}')

m=int(p)-int(q)
n=int(q)-int(p)

print(f' Sonrakı cəmlər: {m} və {n}')
list.append(m)
list.append(n)
print(' Yeni list: ',list)

