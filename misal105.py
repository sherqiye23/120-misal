#105ci sual
#A,B və C təsadüfi ədədlərini yaradın. Tərəfləri bu ədələr olan üçbucaq qurmaq mümkündürsə ekrana bu ədədləri və YES çıxarın. Əgər alınan üçbucaq düzbucaqlı üçbucaqdırsa, ekrana 1, əks halda 0 çıxarın.

while True:
	from math import *
	a = int(input("  a-nın qiymətini daxil edin: "))
	b = int(input("  b-nin qiymətini daxil edin: "))
	c = int(input("  c-nin qiymətini daxil edin: "))
	
	if a+b>c>abs(a-b) and  a+c>b>abs(a-c) and  b+c>a>abs(b-c):
		print(" YES")
	
	else:
		print(" Belə bir üçbucaq mövcud deyil. Kodu yenidən başladıb rəqəmləri yenidən yazın. ")
		break
		
	if b**2+c**2==a**2 or a**2+c**2==b**2 or a**2+b**2==c**2:
		print(" ",1)
		
	elif b**2+c**2!=a**2 or a**2+c**2!=b**2 or a**2+b**2!=c**2:
		print(" ",0)
