#4cü sual
#4 rəqəmli natural ədəd verilmişdir. Onun palindrom ədəd olduğunu təyin edin. Qeyd edək ki, tam ədəd o zaman palindrom sayılır ki, soldan - sağa və əksinə eyni cür oxunur, məs, 2332 ədədi palindrom sayılır.
while True:
	x = input(" 4rəqəmli ədəd yazın: ")
	y = list(x)
	if 999<int(x)<10000:
		z = y[::-1]

		if y == z:
			print(" Palindrom ədəddir.\n")
	
		else:
			print(" Palindrom ədəd deyil.\n")