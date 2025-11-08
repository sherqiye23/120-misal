#65ci sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə rəqəmlərin sayını tapın və onları ekrana çıxarın.
while True:
	x = input(" Birşey yazın: ")
	y = "0123456789"
	a =[]
	for i in x:
		if i in y:
			a.append(i)
	b = len(a)
		
	print(f"Rəqəmlər: {a}, Sayı: {b}",'\n')