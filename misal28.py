#28ci sual
#İkirəqəmli tam müsbət ədəd verilib. Bu ədədin rəqəmlərinin yerini dəyişməklə çıxışa verin.
while True:
	x = input(" 2rəqəmli ədəd yazın: ")
	y=list(x)
	if len(x)==2 and int(x)>0:
		z=y[::-1]
		print(' ',"".join(z), '\n')