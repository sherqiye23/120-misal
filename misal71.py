#71ci sual
#Klaviaturadan ayın nömrəsi daxil edilir. Bu ayda neçə gün olduğunu təyin etmək üçün proqram tərtib edin
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
c = [2]
while True:
	nömrə = int(input(" Ayın nömrəsini yazın: "))
	if nömrə in a:
		print(" Bu ayda 31 gün var.")
	
	elif nömrə in b:
		print(" Bu ayda 30 gün var.")
	
	else:
		print(" Bu ay Fevraldır. Ya 28, ya da 29 gün var.")