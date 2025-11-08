#35ci sual
#Üçbucağın tərəfləri verildikdə onun sahəsini Heron düsuru ilə hesablayın
while True:
	from math import *
	a = float(input("  a-nın qiymətini yazın: "))
	b = float(input("  b-nin qiymətini yazın: "))
	c = float(input("  c-nin qiymətini yazın: "))

	if a == 0 or b == 0 or c == 0:
		print("  Həlli yoxdur!")

	else:
		p = (a+b+c)/2
		s = sqrt(p*(p-a)*(p-b)*(p-c))
	print("  Üçbucağın sahəsi:",s)
