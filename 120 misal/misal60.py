#60cı sual
#N-rəqəmli ədəd daxil edin. Bu ədədin yazılışında yalnız bir dəfə iştirak edən rəqəmləri təyin edin
n=list(input(' Ədəd yazın: '))
list=[n.count('0'),n.count('1'),n.count('2'),n.count('3'),n.count('4'),n.count('5'),n.count('6'),n.count('7'),n.count('8'),n.count('9')]
for i in range(10):
	if list[i]==1:
		print(' 1dəfə iştirak edən:',i)
		
