#106cı sual
#Tutaq ki, 5-rəqəmli pul məbləği verilmişdir. Bu məbləği 200, 100, 50, 20, 10, 5 və 1 manatlıq pul vahidləri ilə xırdaladıqda hər pul vahidindən neçə dənə olacaq?
while True:
	x = int(input(" 5rəqəmli pul məbləğini yazın: "))
	list2 = []
	list = [200, 100, 50, 20, 10, 5, 1]
	for i in range(len(list)):
		while x-list[i]>=0:
			x -= list[i]
			list2.append(list[i])
	print(' 200 manatdan:',list2.count(200))
	print(' 100 manatdan:',list2.count(100))
	print(' 50 manatdan:',list2.count(50))
	print(' 20 manatdan:',list2.count(20))
	print(' 10 manatdan:',list2.count(10))
	print(' 5 manatdan:',list2.count(5))
	print(' 1 manatdan:',list2.count(1))