#33cü sual
#Beşrəqəmli natural ədəd verilib. Bu ədədin ilk iki rəqəminin cəmi ilə son iki rəqəminin cəminin fərqini hesablayın. 
while True:
	x = input("  5rəqəmli ədəd yazın: ")
	if len(x)==5:
		n = (int(x[0]) + int(x[1])) - (int(x[3]) + int(x[4]))
		print("  ",n)