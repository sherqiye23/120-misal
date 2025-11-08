#22ci sual
#N natural ədədi verilmişdir. Həmin ədəddən cüt rəqəmləri silin.
while True:
	n = list(input(" Ədəd yazın: "))
	for i in n:
		if int(i)%2==0:
			n.remove(i)
	print(' ',"".join(n), '\n')