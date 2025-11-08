#5ci sual
#Beşrəqəmli natural ədəd verilmişdir. Ən solda yerləşən rəqəmdən başlayaraq bütün rəqəmlərin artma sırası ilə yerləşdiyini  müəyyən etmək lazımdır.  Məsələn, 15689 ədədində bütün rəqəmlər artma sırası ilə yerləşir.
while True:
	a = input(" 5rəqəmli ədəd yazın: ")
	if 9999<int(a)<100000:
		if a[0]<a[1]<a[2]<a[3]<a[4]:
			print(" Bu şərt ödənilir.\n")
	
		else:
			print(" Bu şərt ödənilmir.\n")
