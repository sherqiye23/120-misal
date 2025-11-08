#15ci sual
#N natural ədədi verilmişdir. Onun polindrom olub olmamasını müəyyən edin. Polindrom olduqda  "YES" , əks halda "NO" çıxışa verin.
while True:
	x = list(input("  Natural ədəd yazın: "))
	z = x[::-1]

	if x == z:
		print("  YES\n")	
	else:
		print("  NO\n")