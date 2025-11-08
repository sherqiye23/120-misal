#100cü sual
#N elementdən ibarət siyahı verilmişdir.Bu siyahıda A[1] → A[2]; A[2] → A[3]; ... A[n] → A[1] yerdəyişməsini aparmaqla alına siyahını ekrana çıxarın. 
while True:
	a = list(input(' Siyahı yazın: '))
	b=a[-1]
	a.pop(-1)
	a.insert(0,b)
	print(a)