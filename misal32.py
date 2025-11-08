#32ci sual
#999-dan böyük tam ədəd verilib. Bir qalıqsız bölmə (//) və bir bölmənin qalığını alma (%) əməlindən istifadə etməklə həmin ədədin yazılışındakı minlik mərtəbənin rəqəmini tapın. 
while True:
	num = int(input(" 4 rəqəmli ədəd yazın: "))
	if num > 999:
		c = num//1000
		if c>9:
			print(" ",str(c)[-1])
		else:
			print(" ",c)