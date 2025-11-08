#27ci sual
#Üçrəqəmli natural ədəd verilib. Bu ədədin rəqəmləri arasına boşluq simvolu qoymaqla çıxışa verin.
while True:
	x = input(" 3rəqəmli ədəd yazın: ")
	a = ''
	if len(x)==3:
		for i in range(len(x)):
			a = a + x[i] + ' '
		print(' ',a, '\n')