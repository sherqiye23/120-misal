#52ci sual
#ax+b=c şəklində verilmiş xətti tənliyin a,b və c-nin ixtiyari qiyməti üçün həlli
while True:
	a = float(input(" a-nın qiymətini yazın: "))
	b = float(input(" b-nin qiymətini yazın: "))
	c = float(input(" c-nin qiymətini yazın: "))
	#ax + b = c
	if a==0:
		print(" Həlli yoxdur", '\n')
	else:
		x = (c-b)/a
		print(f"  x: {x} ", '\n')