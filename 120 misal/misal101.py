#101ci sual
#N elementdən ibarət siyahı verilmişdir.Bu siyahıda tək nömrəli elementləri cüt nömrəli elementlərlə əvəz edin : A[1] ↔ A[2]; A[3] ↔ A[4] ...
while True:
	a = list(input(' Siyahı yazın: '))
	for i in range(0,len(a)-1,2):
		(a[i], a[i+1]) = (a[i+1], a[i])
	print(a)