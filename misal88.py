#88ci sual
#Tək sayda ədədlərdən ibarət siyahı  verilmişdir. Bu siyahıda ortadakı elementdən sağda və solda yerləşən elementləri cəmləyin. Hansı kiçikdirsə, ortadakı ədədi həmin cəmlə əvəz edin.

def toplama(list):
	sum = 0
	for i in list:
		sum += i
	return sum

from random import*
list=[randint(1,100) for k in range(9)]
print(list)
ilkCəm = toplama(list[:round((len(list))/2)])
ikinciCəm = toplama(list[round((len(list)+1)/2):])
if ilkCəm < ikinciCəm:
	list[round(len(list)/2)] = ilkCəm
else:
	list[round(len(list)/2)] = ikinciCəm		

print(list)