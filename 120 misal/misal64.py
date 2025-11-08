#64cü sual
#İstənilən uzunluqlu sətir verilmişdir. Bu sətirdə kiçik hərflərin sayını tapın və onları ekrana çıxarın.
while True:
	x = input(" Birşey yazın: ")
	y = "qüertyuiopöğasdfghjklıəzxcvbnmçşw"
	a =[]
	for i in x:
		if i in y:
			a.append(i)
	b = len(a)
		
	print(f"Kiçik hərflər: {a}, Sayı: {b}", '\n')