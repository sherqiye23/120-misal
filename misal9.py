#9cu sual
#Üç tam ədəd verilib. Onların arasında eyni olduqlarının sayını müəyyən edin. Əgər üçü də eynidirsə, çıxışa 3 rəqəmi, ikisi eynidirsə - 2, ədədlər fərqlidirsə 0 rəqəmi verin. 
while True:
	a = int(input(" 1ci rəqəmi yazın: "))
	b = int(input(" 2ci rəqəmi yazın: "))
	c = int(input(" 3cü rəqəmi yazın: "))

	if a == b == c:
		print(" 3")
	
	elif a==b or b==c or a==c:
		print(" 2")
	
	else:
		print(" 0")

