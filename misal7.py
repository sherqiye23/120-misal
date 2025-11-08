#7ci sual
#4-rəqəmli natural ədədi verilmişdir. Bu ədədin yazılışından cüt rəqəmləri silin (0 - cüt rəqəm kimi qəbul edin).
while True:
	x = (input(" 4rəqəmli ədəd yazın: "))
	y = list(x)
	if 999<int(x)<10000:
		for i in x:
			if int(i)%2==0:
				y.remove(i)
		print(" ","".join(y))
	