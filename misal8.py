#8ci sual
#Dördrəqəmli natural ədəd verilib. Onun rəqəmlərinin bir birindən fərqli olduğunu müəyyən edin. Əgər fərqlidirsə, "YES" çıxışa verin, əks halda - "NO".
while True:
	x = input("  4rəqəmli ədəd yazın: ")
	y = list(x)
	if 999<int(x)<10000:
		a = int(x[0])
		b = int(x[1])
		c = int(x[2])
		d = int(x[3])

		if a != b and a != c and a != d and b != c and b != d and c != d:
			print("  YES")
	
		else:
			print("  NO")