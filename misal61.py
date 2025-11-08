#61ci sual
#Rəqəmlərinin cəmi rəqəmlərinin hasilinə bərabər olan bütün 5-rəqəmli ədədləri tapıb ekrana çıxarın
n=list(input(' Ədəd yazın: '))
list=[n.count('0'),n.count('1'),n.count('2'),n.count('3'),n.count('4'),n.count('5'),n.count('6'),n.count('7'),n.count('8'),n.count('9')]
for i in range(10):
	if list[i]==2:
		print(' 2dəfə iştirak edən:',i)