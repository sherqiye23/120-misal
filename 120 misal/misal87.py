#87ci sual
#Cüt sayda ədədlərdən ibarət siyahı və M-ədədi verilmişdir. Bu siyahının birinci və ikinci yarısının elementlərini cəmləyin. Hansı böyükdürsə, M ədədini həmin yarim hissənin əvvəlinə əlavə edin.
while True:
	from random import*
	def toplama(list):
		sum = 0
		for i in list:
			sum += i
		return sum
	
	m=int(input(" M-i yazın: "))	
	list=[randint(1,100) for k in range(10)]
	print(list)

	ilkCəm = toplama(list[:round(len(list)/2+1)])
	print('  ',ilkCəm)
	ikinciCəm = toplama(list[round(len(list)/2):])
	print('  ',ikinciCəm)

	if ilkCəm > ikinciCəm:
		list.insert(0,m)
	if ilkCəm < ikinciCəm:
		list.insert(len(list)/2,m)

	print(list)
	