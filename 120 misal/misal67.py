#67ci sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə görünməz  simvolların sayını tapın və onların sətirdəki mövqeyini ekrana çıxarın.
while True:
	x = input(" Birşey yazın: ")
	y = "	 "
	a =[]
	for i in x:
		if i in y:
			a.append(i)
	b = len(a)
		
	print(f"Görünməz simvollar: {a}, Sayı: {b}",'\n')