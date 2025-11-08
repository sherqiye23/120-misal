#20ci sual
#N natural ədədi verilmişdir. Həmin ədəddə tək rəqəmlərin sayını tapın. (0 tək ədəd sayılmır)
while True:
	n= list(input(" Ədədi yazın: "))
	a =[]
	for i in n:
		if int(i)%2 != 0:
			a.append(i)			
	print(" ",len(a))