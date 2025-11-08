#90cı sual
#Mənfi və müsbət ədədlərdən ibarət siyahı verilmişdir. Siyahıya elə elementlər daxil edin ki, müsbət elementlərin sayı mənfi elementlərin sayına  bərabər olsun.
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

x = len(musbet)-len(menfi)
if x>0:
	for k in range(x):
		list.append(-1)
elif x<0:
	for k in range(abs(x)):
		list.append(1)
print(list)