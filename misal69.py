#69cu sual
#Verilmiş cümlədə bütün sözlərin arasında * simvolu qoymaqla alınan cümləni ekrana çıxarın.
while True:
	x = input(' Cümlə yazın: ')
	y = list(x)
	for i in range(len(x)):
		if x[i] == ' ':
			y[i] = '*'
	y = ''.join(y)
	print(' ',y)