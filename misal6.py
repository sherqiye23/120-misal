#6cı sual
#4-rəqəmli tam müsbət ədəd verilmişdir.Bu ədədin öz rəqəmlərin hamısına bölündüyünü təyin edin.	
while True:
	n = int(input(" 4rəqəmli ədəd yazın: "))
	if 999<int(n)<10000:
		a = int(str(n)[0])
		b = int(str(n)[1])
		c = int(str(n)[2])
		d = int(str(n)[3])

		if n%a==0 and n%b==0 and n%c==0 and n%d==0:
			print(" Bu ədəd öz rəqəmlərinə bölünür.\n")
		else:
			print(" Bu ədəd öz rəqəmlərinə bölünmür.\n")
	
	else:
		print(" Bu ədəd 4rəqəmli deyil.\n")