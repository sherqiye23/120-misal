#54cü sual
#Beşrəqəmli tam ədədinin daxil edin. Onun rəqəmlərinin hasilini tapın.
while True:
	x = input("  5rəqəmli ədəd yazın: ")
	if len(x)==5:
		hasil=1
		for i in x:
			hasil*=int(i)
		print(' ',hasil, '\n')