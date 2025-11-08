#85ci sual
#Ədədlərdən ibarət siyahı verilmişdir. Bu siyahıda 3-cü elementdən başlayaraq 0-rəqəmi varsa, onu əvvəlki iki elementin cəmi ilə əvəz edin
while True:
	n = list(input(" Ədədlərdən ibarət siyahı yazın: "))
	for i in range(2, len(n)):
		if n[i] == "0":
			n[i] = str(int(n[i-1]) + int(n[i-2]))
	print(n)