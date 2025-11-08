#2ci sual
#X, Y (Y  ≠   X) iki həqiqi ədəd verilmişdir. Ədədlərin kiçiyini həmin ədədlərin cəminin yarısı ilə, böyüyünü isə bu ədədlərin iki misli ilə əvəz edin.
while True:
	x = int(input("  x-ın qiymətini yazın: "))
	y = int(input("  y-in qiymətini yazın: "))

	a = (x+y)/2
	b = (x+y)*2

	if x < y:
		x = a
		y = b
	
	elif x > y:
		x = b
		y = a
	
	else:
		print("x və y bərabər olmamalıdır!")
	
	print("  X =",x)
	print("  Y =",y, '\n')