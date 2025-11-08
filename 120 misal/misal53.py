#53cü sual
#Beşrəqəmli tam ədədinin daxil edin. Onun ən kiçik rəqəminin ədəddə neçə dəfə iştirak etdiyini təyin edin
while True:
	a = input("  5rəqəmli ədəd yazın: ")
	b = list(a)
	if len(a)==5:
		print(" Ən kiçik rəqəm", min(b))
		print(" Sayı", b.count(min(b)))
