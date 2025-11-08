#63cü sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə böyük hərflərin sayını tapın və onları ekrana çıxarın.
while True:
	x = input(" Birşey yazın: ")
	y = "QÜERTYUİOPÖĞASDFGHJKLIƏZXCVBNMÇŞW"
	a =[]
	for i in x:
		if i in y:
			a.append(i)
	b = len(a)
		
	print(f"Böyük hərflər: {a}, Sayı: {b}", '\n')