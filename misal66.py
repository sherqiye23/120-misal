#66cı sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə hərf və rəqəm olmayan simvolların sayını tapın və onları ekrana çıxarın.
while True:
	x = input(" Birşey yazın: ")
	y = "0123456789qüertyuiopöğasdfghjklıəzxcvbnmçşwQÜERTYUİOPÖĞASDFGHJKLIƏZXCVBNMÇŞW"
	a =[]
	for i in x:
		if i not in y:
			a.append(i)
	b = len(a)
		
	print(f"Simvollar: {a}, Sayı: {b}", '\n')