#30cu sual
#Üçrəqəmli tam ədəd verilib. Onun soldan birinci rəqəmini pozub ədədin sağına yazdılar. Alınan ədədi çıxışa verin.
while True:
	x = input(" 3rəqəmli ədəd yazın: ")
	y = list(x)
	if len(x)==3:
		a = y.pop(0)
		y.append(a)
	print(' ',"".join(y), '\n')
