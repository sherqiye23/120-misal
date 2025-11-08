#3cü sual
#Üçrəqəmli natural ədəd verilib. Onun Armstronq ədədi olub-olmadığını müəyyən edin. (Armstronq ədədində rəqəmlərin 3-cü qüvvətinin cəmi həmin ədədə bərabərdir. Məsələn, 153 ədədi Armstronq ədədidir, çünki  153 = 1³+5³+3³).
while True:
	x = input(" 3rəqəmli ədəd yazın: ")
	y=0
	if len(x)==3:
		for i in str(x):
			y+=int(i)**3
		if int(y)==int(x):
			print(" Bu ədəd armstronq ədədidir.\n")
		else:
			print(" Bu ədəd armstronq ədədi deyil.\n")