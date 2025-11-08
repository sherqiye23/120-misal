#13cü sual
#N natural ədədi verilmişdir. Rəqəmləri əks ardıcıllığı ilə yerləşən yeni M ədədi alın.  Məsələn, əgər 123456 ədədi verilibsə, nəticədə 654321 ədədi alınmalıdır.
while True:
	n = input(" Ədəd yazın: ")
	print(" n =",n)
	x=list(n)
	m = x[::-1]
	print(" m =","".join(m), '\n')