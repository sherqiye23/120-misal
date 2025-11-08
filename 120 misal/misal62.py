#62ci sual
#Rəqəmlərinin cəmi rəqəmlərinin hasilinə bərabər olan bütün 5-rəqəmli ədədləri tapıb ekrana çıxarın
list =[]
for x in range(10000, 100000): 
	a = int(str(x)[0])+int(str(x)[1])+int(str(x)[2])+int(str(x)[3])+ int(str(x)[4])
	b = int(str(x)[0])*int(str(x)[1])*int(str(x)[2])*int(str(x)[3])*int(str(x)[4])

	if a == b:
		list.append(x)

print(list)