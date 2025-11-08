#29cu sual
#Üçrəqəmli tam ədəd verilib. Bu ədədin rəqəmlərini sağdan sola oxuduqda alınan ədədi çıxışa verin.
while True:
	x = input(" 3rəqəmli ədəd yazın: ")
	y = list(x)
	if len(x)==3:
		z = y[::-1]
		print(' ',"".join(z),'\n')