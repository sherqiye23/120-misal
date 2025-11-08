#68ci sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə boşluq simvollarını(probelləri) *-simvolu ilə əvəz edib alınan nəticəni ekrana çıxarın .
while True:
	x = input(' Cümlə yazın: ')
	y = list(x)
	for i in range(len(x)):
		if x[i] == ' ' or x[i]=='\t':
			y[i] = '*'
	y = ''.join(y)
	print(' ',y)