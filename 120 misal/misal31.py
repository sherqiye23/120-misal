#31ci sual
#Üçrəqəmli tam ədəd verilib. Bu ədədin yüzlüklərinin və onluqlarının yerini dəyişməklə alınan ədədi çıxışa verin. 
while True:
	x = input(" 3rəqəmli ədəd yazın: ")
	y = list(x)
	if 99<int(x)<1000:
		z =y[::-1]
		a = z.pop(0)
		z.append(a)
	print(" ","".join(z))