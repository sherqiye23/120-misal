#104cü sual
#A,B və C təsadüfi ədədlərini yaradın. Tərəfləri bu ədələr olan üçbucaq qurmaq mümkündürsə ekrana bu ədədləri və YES çıxarın. Əks halda,  bu ədədlərdən ibarət üçbucaq qurmaq mümkün olana qədər prosesi təkrar edin.
while True:
	from math import *
	a = int(input("  a-nın qiymətini daxil edin: "))
	b = int(input("  b-nin qiymətini daxil edin: "))
	c = int(input("  c-nin qiymətini daxil edin: "))

	if a+b>c>abs(a-b) and  a+c>b>abs(a-c) and  b+c>a>abs(b-c):
		print(" YES")
	
	else:
		print(" Belə bir üçbucaq mövcud deyil. Rəqəmləri yenidən daxil edin. ")