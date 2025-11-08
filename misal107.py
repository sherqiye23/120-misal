#107ci sual
#Tərəfləri a, b və c olan yeşik verilmişdir. Bu yeşiyi ölçüləri m x n olan qapıdan keçirmək olarmı?
while True:
	a = float(input(" a-nı yazın: "))
	b = float(input(" b-ni yazın: "))
	c = float(input(" c-ni yazın: "))

	m = float(input(" m-i yazın: "))
	n = float(input(" n-i yazın: "))

	if a*b <= m*n or b*c <= m*n or a*c <= m*n:
		print(' Qapıdan keçəcək.\n')
	else:
		print(' Qapıdan keçməyəcək.\n')